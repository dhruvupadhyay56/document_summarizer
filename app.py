from langchain_ollama import ChatOllama
from langchain_community.text_splitter import RecursiveCharacterTextSplitter # type: ignore
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.chains.summarize import load_summarize_chain # type: ignore
from langchain_community.document_transformers import EmbeddingsClusteringFilter
from langchain.embeddings import HuggingFaceBgeEmbeddings
from chunking import chunk_text
from summarizer import summarize_chunk, generate_final_summary


def extract(file_path):
    loader = PyPDFLoader(file_path)
    pages = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=2000, chunk_overlap=0
    )
    texts = text_splitter.split_documents(pages)
    return texts


def chunk_text(text, chunk_size=2000, overlap=200):
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap

    return chunks

from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize_chunk(chunk):
    prompt = f"""
    Summarize this document chunk:

    {chunk}
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

def generate_final_summary(chunk_summaries):
    combined = "\n".join(chunk_summaries)

    prompt = f"""
    Create a structured summary with:

    1. Executive Summary
    2. Key Points
    3. Risks or Concerns
    4. Opportunities
    5. Action Items

    Here is the content:
    {combined}
    """   

from pdf_reader import extract_text
from chunking import chunk_text
from summarizer import summarize_chunk, generate_final_summary

text = extract_text("sample.pdf")

chunks = chunk_text(text)

chunk_summaries = []

for chunk in chunks:
    summary = summarize_chunk(chunk)
    chunk_summaries.append(summary)

final_summary = generate_final_summary(chunk_summaries)

print(final_summary)