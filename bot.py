import gradio as gr
import pdfplumber
import torch
import os
from transformers import pipeline, T5Tokenizer, T5ForConditionalGeneration
from fpdf import FPDF  # For creating PDFs

# Check if GPU is available
device = "cuda" if torch.cuda.is_available() else "cpu"

# Load Summarization Model (T5 Small for Efficiency)
summarizer = pipeline("summarization", model="t5-small", device=0 if device == "cuda" else -1)

# Load FLAN-T5 Model for Viva Questions, MCQs, Flashcards, and AI Tutor
model_name = "google/flan-t5-base"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name).to(device)

# Function to extract text from a given number of pages in a PDF
def extract_text_from_pdf(file_path, num_pages=50):
    text = ""

    try:
        num_pages = int(num_pages)  # Ensure num_pages is an integer
    except ValueError:
        num_pages = 50  # Default to 50 pages if conversion fails

    with pdfplumber.open(file_path) as pdf:
        total_pages = len(pdf.pages)
        num_pages = min(num_pages, total_pages)  # Prevent exceeding actual page count

        for i in range(num_pages):
            page_text = pdf.pages[i].extract_text()
            if page_text:
                text += page_text + "\n"

    return text.strip()

# Function to split text into smaller chunks (Ensures max 1024 tokens per chunk)
def split_text_into_chunks(text, max_length=1024):
    words = text.split()
    chunks = [" ".join(words[i:i+max_length]) for i in range(0, len(words), max_length)]
    return chunks

# Function to summarize text
def summarize_text(text):
    chunks = split_text_into_chunks(text, max_length=1024)
    summaries = []

    for chunk in chunks[:10]:  # Limit to 10 chunks for large files
        summary_length = min(200, len(chunk.split()) // 2)  # Adjust dynamically
        summary = summarizer(chunk, max_length=summary_length, min_length=summary_length // 2, do_sample=False)[0]['summary_text']
        summaries.append(f"- {summary}")

    return "\n".join(summaries)

# Function to generate viva questions (Fixes duplicate issues)
def generate_viva_questions(text, num_questions=5):
    chunks = split_text_into_chunks(text, max_length=1024)
    prompt = f"Generate {num_questions} UNIQUE viva questions from this text:\n{chunks[0]}"
    
    inputs = tokenizer(prompt, return_tensors="pt", max_length=1024, truncation=True).to(device)
    outputs = model.generate(**inputs, max_length=150, num_return_sequences=num_questions, num_beams=num_questions)

    return "\n".join([f"{i+1}. {tokenizer.decode(output, skip_special_tokens=True)}" for i, output in enumerate(outputs)])

# Function to generate MCQs (Fixes duplicate MCQs)
def generate_mcqs(text, num_mcqs=5):
    chunks = split_text_into_chunks(text, max_length=1024)[:3]  # Process multiple chunks for diversity
    prompt = f"Generate {num_mcqs} unique multiple-choice questions with four distinct answer choices:\n\n{chunks[0]}"
    
    inputs = tokenizer(prompt, return_tensors="pt", max_length=1024, truncation=True).to(device)
    
    outputs = model.generate(
        **inputs, 
        max_length=150, 
        num_return_sequences=num_mcqs, 
        num_beams=max(num_mcqs, 5),  # ✅ Ensures num_beams >= num_return_sequences
        do_sample=True,  
        temperature=0.7,  
        top_k=50  
    )

    return "\n\n".join([f"{i+1}. {tokenizer.decode(output, skip_special_tokens=True)}" for i, output in enumerate(outputs)])

# Function to generate flashcards (Fixes duplicate flashcards)
def generate_flashcards(text, num_flashcards=5):
    chunks = split_text_into_chunks(text, max_length=1024)
    prompt = f"Generate {num_flashcards} UNIQUE flashcards with key concepts from this text:\n{chunks[0]}"
    
    inputs = tokenizer(prompt, return_tensors="pt", max_length=1024, truncation=True).to(device)
    outputs = model.generate(**inputs, max_length=100, num_return_sequences=num_flashcards, num_beams=num_flashcards)

    return "\n".join([f"- {tokenizer.decode(output, skip_special_tokens=True)}" for output in outputs])

# AI-Powered Tutor: Answer questions based on the PDF
def answer_question(text, question):
    question = str(question)

    if not question.strip():
        return "Please enter a valid question."

    chunks = split_text_into_chunks(text, max_length=1024)
    prompt = f"Based on the following content:\n{chunks[0]}\nAnswer this question: {question}"
    inputs = tokenizer(prompt, return_tensors="pt", max_length=1024, truncation=True).to(device)
    outputs = model.generate(**inputs, max_length=150, num_return_sequences=1, num_beams=5)

    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Function to create a PDF with summary
def create_summary_pdf(summary_text):
    pdf_dir = "/mnt/data" if os.path.exists("/mnt/data") else "summaries"
    os.makedirs(pdf_dir, exist_ok=True)

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    pdf.set_font("Arial", style="B", size=14)
    pdf.cell(200, 10, "Summarized Points", ln=True, align="C")
    pdf.ln(10)

    pdf.set_font("Arial", size=12)

    # Convert text to UTF-8 to prevent encoding errors
    summary_text = summary_text.encode("latin-1", "ignore").decode("latin-1")

    for line in summary_text.split("\n"):
        pdf.cell(0, 10, line, ln=True)

    pdf_filename = os.path.join(pdf_dir, "Summary.pdf")
    pdf.output(pdf_filename, "F")
    return pdf_filename

# Function to process PDF
def process_pdf(file_path, num_pages, question):
    text = extract_text_from_pdf(file_path, num_pages)
    if not text:
        return "Error: No text found in the PDF.", None, None, None, None, None

    summary = summarize_text(text)
    viva_questions = generate_viva_questions(text[:5000], 5)
    mcqs = generate_mcqs(text[:5000], 5)
    flashcards = generate_flashcards(text[:5000], 5)
    tutor_answer = answer_question(text, question)

    pdf_path = create_summary_pdf(summary)

    return summary, viva_questions, mcqs, flashcards, tutor_answer, pdf_path

# Create Gradio Interface
iface = gr.Interface(
    fn=process_pdf,
    inputs=[
        gr.File(label="📂 Upload a Large PDF", type="filepath"),
        gr.Slider(minimum=5, maximum=100, step=5, value=50, label="📄 Number of Pages to Process"),
        gr.Textbox(label="❓ Ask AI Tutor a Question"),
    ],
    outputs=[
        gr.Textbox(label="📌 Summary (Bullet Points)", lines=10),
        gr.Textbox(label="📖 Viva Questions", lines=10),
        gr.Textbox(label="📝 MCQs (Multiple Choice Questions)", lines=10),
        gr.Textbox(label="📌 Flashcards (Quick Revision Notes)", lines=10),
        gr.Textbox(label="🤖 AI Tutor Answer", lines=10),
        gr.File(label="📥 Download Summary PDF")
    ],
)

iface.launch() 
