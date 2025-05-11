import streamlit as st
import pdfplumber
from transformers import pipeline
from summa import summarizer

####### function responsible for text chunking #######
def split_text(text, chunk_size=3000, overlap=200):
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunk = text[start:end]
        if chunk.strip():  # Avoid empty chunks
            chunks.append("summarize: " + chunk)
        start += chunk_size - overlap
    return chunks

# Change background color
st.markdown(
    """
    <style>
    .stApp {
        background-color: #260638;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Add title and image at the top
# Create two columns: title on left, image on right
col1, col2 = st.columns([4, 3])  # Wider title, narrower image

with col1:
    st.markdown("<h1 style='margin-bottom: 0;'>📄 STUDENT SCRIBE</h1>", unsafe_allow_html=True)

with col2:
    st.image("https://img.freepik.com/free-vector/graident-ai-robot-vectorart_78370-4114.jpg?semt=ais_hybrid&w=740", width=120)


# Uploading of PDF file
uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

pdf_text = ""  # Variable to store extracted text

if uploaded_file is not None:
    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            pdf_text += page.extract_text() or ""  # Handle pages with no text

    st.success("Text extracted successfully!")

# You can use `pdf_text` however you want afterward

#######             main summarization logic            #######
##     this calls the split_text function defined above      ##

    pdf_text_chunks = split_text(pdf_text)

    summarizer = pipeline("summarization", model="t5-small")
    summaries = [summarizer(chunk, max_length=150, min_length=50, do_sample=False)[0]['summary_text']
                  for chunk in pdf_text_chunks]
    final_summary = ' '.join(summaries)
    #summary_text = summary[0]['summary_text']
    st.subheader("Extracted Text (Preview)")
    st.text_area("Text", pdf_text[:], height=300)

    st.subheader("Summarized Text (Preview)")
    st.text_area("Summarized Text", final_summary[:], height=300)



