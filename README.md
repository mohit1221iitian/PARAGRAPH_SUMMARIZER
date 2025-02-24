# **AI-Powered PDF Summarizer & Tutor** 📚🤖

Welcome to the **AI-Powered PDF Summarizer & Tutor** project! 🚀 This tool allows you to upload a PDF document, extract and summarize key points, generate viva questions, multiple-choice questions (MCQs), flashcards, and interact with an AI-powered tutor to get answers from the document. Everything is powered by cutting-edge machine learning models, making this a must-have for students and educators alike! 🎓💡

---

## **Features** 📋✨
- **PDF Text Extraction**: Extracts text from PDFs (up to 100 pages).
- **Summarization**: Get a summary of the document in bullet points.
- **Viva Questions**: Automatically generates relevant viva questions from the text.
- **MCQs**: Generate multiple-choice questions to test your knowledge.
- **Flashcards**: Create quick revision notes for efficient learning.
- **AI Tutor**: Ask questions about the content, and the AI will provide answers! 🤖

---

## **Technologies Used** 🛠️

- **Gradio**: For creating the user interface. 🌐
- **PDFplumber**: For extracting text from PDF files. 📄
- **Hugging Face Transformers**: For natural language processing (NLP) tasks like summarization, question generation, and more. 🧠
- **PyTorch**: For running machine learning models. ⚡
- **FPDF**: For generating downloadable summary PDFs. 📥

---

## **Getting Started** 🚀

To run this project locally, follow these steps:

### **1. Clone the Repository** 📂
bash
git clone https://github.com/mohit1221iitian/PARAGRAPH_SUMMARIZER.git

### Prerequisites 📦

Make sure you have the following installed on your system:
- **Python 3.6 or higher** ✨
- **Pip** (Python package manager) 🔧



### *2️⃣ Install Dependencies*
Make sure you have *Python 3.10+* installed, then run:
bash
pip install -r requirements.txt


### *3️⃣ Run the Application Locally*
bash
python bot.py

This will launch the *Gradio UI* in your browser at http://127.0.0.1:7860

---


🚀 *Try it live here:* https://huggingface.co/spaces/mohit-me/EDUCATION_BOT

## **How to Use** 🎬

1. **Upload a PDF**: Click the “📂 Upload a Large PDF” button to select the PDF document you want to analyze.
2. **Choose Number of Pages**: Use the slider to specify how many pages you want to process (default is 50).
3. **Ask a Question**: Type a question related to the content of the PDF, and the AI Tutor will provide an answer.
4. **Get Results**:
    - **Summary**: View a summarized version of the document in bullet points.
    - **Viva Questions**: Automatically generate viva questions.
    - **MCQs**: Receive multiple-choice questions based on the document.
    - **Flashcards**: Create revision flashcards.
    - **AI Tutor**: Get answers from the AI Tutor based on the document's content.
5. **Download Summary PDF**: After summarizing, you can download the summary in PDF format.

---

## **Example Output** 📝

After uploading a PDF, the output could look like this:

### **📌 Summary**
- Key points and highlights of the document.
- Helps you get the main ideas in a few sentences.

### **📖 Viva Questions**
1. What are the key themes discussed in the document?
2. Explain the significance of [topic] in relation to [subject].

### **📝 MCQs**
1. What is the primary function of [concept]?
   - A) Option 1
   - B) Option 2
   - C) Option 3
   - D) Option 4

### **📌 Flashcards**
- What is the definition of [term]?
- What are the key takeaways from [section]?

### **🤖 AI Tutor Answer**
- The AI answers your specific questions based on the text from the PDF.

## 📂 Project Structure

PARAGRAPH_SUMMARIZER/
│── app.py                # Main application file (Gradio UI)
│── requirements.txt      # Required dependencies
│── README.md             # Project documentation
│── model/                # (Optional) Local model files


---

## Screenshots

## 🤝 Contributing
Feel free to *fork* this repository and improve the project. Contributions are welcome!

---

## 📜 License
This project is *MIT Licensed*. You are free to use, modify, and distribute it.

---

### 🔗 Connect with Me
- GitHub: https://github.com/mohit1221iitian/PARAGRAPH_SUMMARIZER


🚀 *Happy Coding!*
