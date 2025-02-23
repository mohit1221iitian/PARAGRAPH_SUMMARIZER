import gradio as gr
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline

# Use the correct Hugging Face model path
MODEL_PATH = "facebook/bart-large-cnn"  # ✅ Fixed!

# Load the model and tokenizer
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_PATH)

# Create summarization pipeline
summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)

# Function to summarize text
def summarize_text(user_input):
    if not user_input.strip():
        return "⚠ Please enter some text to summarize."
    summary = summarizer(user_input, max_length=100, min_length=30, do_sample=False)
    return summary[0]["summary_text"]

# Create Gradio UI
iface = gr.Interface(fn=summarize_text, inputs="text", outputs="text", title="Text Summarization Bot")

# Run the app
if _name_ == "_main_":
    iface.launch()