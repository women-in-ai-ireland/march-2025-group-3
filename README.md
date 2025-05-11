
# Student Scribe

**Student Scribe** is a user-friendly text summarizer tool built using Python and Streamlit. It allows students to upload PDF files and receive AI-generated summaries from large academic documents, research papers, or notes — all with a clean interface and smart summarization powered by a pre-trained `T5` model.

---

## 🚀 Features

- 📄 Upload PDF documents directly
- 🔍 Extracts and previews full text from the PDF
- ✂️ Automatically chunks large text into manageable parts
- 🤖 Uses `t5-small` transformer model for high-quality summarization
- 🎨 Includes custom background color and AI-themed branding
- 📱 Responsive UI using Streamlit columns and markdown

## 📦 Requirements
- Python 3.7+
- Streamlit
- Transformers (pip install transformers)
- pdfplumber
- torch (for model backend)

## ▶️ Usage
To start the app:
streamlit run pdf_summarizer.py

## 🧠 How It Works
1. Upload a PDF: The app uses pdfplumber to extract raw text from all pages.
2. Text Chunking: Large PDFs are split into smaller text blocks (~3000 characters each) with overlap.
3. Summarization: Each chunk is summarized using the Hugging Face t5-small model.
4. Output: Both original and summarized texts are shown in preview boxes.
