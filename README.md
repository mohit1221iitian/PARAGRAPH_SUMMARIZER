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
git clone 

# Installation Instructions ⚙️

### Prerequisites 📦

Make sure you have the following installed on your system:
- **Python 3.6 or higher** ✨
- **Pip** (Python package manager) 🔧

### Clone the Repository 🖥️

To get started, clone the repository to your local machine:

bash
https://github.com/mohit1221iitian/PARAGRAPH_SUMMARIZER.git
cd PDF_SUMMARIZER

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


## 📂 Project Structure

PARAGRAPH_SUMMARIZER/
│── app.py                # Main application file (Gradio UI)
│── requirements.txt      # Required dependencies
│── README.md             # Project documentation
│── model/                # (Optional) Local model files


---

## 🤖 Example Usage
### *Input Paragraph:*
> Critical thinking is an essential skill that plays a vital role in education and lifelong learning. It enables individuals to analyze information, evaluate different perspectives, and make informed decisions based on logic and evidence. In the modern world, where information is abundant but not always reliable, the ability to think critically is more important than ever. Students who develop strong critical thinking skills can differentiate between credible sources and misleading information, which is crucial in academic research, news consumption, and decision-making in daily life. Moreover, critical thinking promotes problem-solving abilities, encouraging students to think independently rather than simply memorizing facts. Instead of passively accepting knowledge, learners are encouraged to ask questions, challenge assumptions, and engage in meaningful discussions. This leads to deeper comprehension, improved creativity, and the ability to adapt to new challenges. Teachers play a crucial role in fostering critical thinking by designing activities that require students to analyze case studies, debate different viewpoints, and apply knowledge to real-world scenarios. Additionally, technology and digital tools provide new opportunities for developing critical thinking through interactive simulations, online discussions, and problem-based learning environments. By incorporating these strategies, educators can help students become more analytical, reflective, and prepared for the complexities of the real world. Ultimately, critical thinking empowers learners with the ability to think independently, solve problems efficiently, and make well-informed decisions, which are essential skills for both academic success and personal growth.

### *Output Summary:*
>In the modern world, where information is abundant but not always reliable, the ability to think critically is more important than ever. Teachers play a crucial role in fostering critical thinking by designing activities that require students to analyze case studies. Technology and digital tools provide new opportunities for developing critical thinking through interactive simulations, online discussions, and problem-based learning environments.

---

## 🤝 Contributing
Feel free to *fork* this repository and improve the project. Contributions are welcome!

---

## 📜 License
This project is *MIT Licensed*. You are free to use, modify, and distribute it.

---

### 🔗 Connect with Me
- GitHub: https://github.com/mohit1221iitian/PARAGRAPH_SUMMARIZER


🚀 *Happy Coding!*
