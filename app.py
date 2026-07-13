import os
import tempfile
import streamlit as st

from pdf_reader import extract_text
from chunking import chunk_text
from summarizer import summarize_chunk, generate_final_summary

st.set_page_config(
    page_title="Document Summarizer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Document Summarizer")

uploaded_file = st.file_uploader(
    "Upload a PDF",
    type=["pdf"]
)

if uploaded_file:

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
        temp_pdf.write(uploaded_file.read())
        pdf_path = temp_pdf.name

    try:

        with st.spinner("Extracting text..."):
            text = extract_text(pdf_path)

        if not text.strip():
            st.error("No readable text found inside the PDF.")
            st.stop()

        with st.spinner("Splitting document..."):
            chunks = chunk_text(text)

        summaries = []

        progress = st.progress(0)

        for index, chunk in enumerate(chunks):
            summary = summarize_chunk(chunk)
            summaries.append(summary)

            progress.progress((index + 1) / len(chunks))

        with st.spinner("Generating final summary..."):
            final_summary = generate_final_summary(summaries)

        st.success("Summary Generated!")

        st.subheader("Final Summary")

        st.markdown(final_summary)

    except Exception as e:
        st.error(f"Error: {e}")

    finally:
        if os.path.exists(pdf_path):
            os.remove(pdf_path)
