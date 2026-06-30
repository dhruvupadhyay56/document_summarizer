This project is an AI-powered document summary creation tool. 
It processes large PDF files and generates structed summaries. 
It uses a chunking strategy and combines chunk summaries into a final structured output
Features:- 
   Upload and process PDF documents
   Extract text from multiple pages
   Chunk large documents to handle token limitations
   Generate summaries for each chunk
   Combine chunk summaries into a final report
   Optional Streamlit UI for file uploads

The data is generated in the structure of Executive Summary, Key Points, Concerns, Opportunities and Action Items.

Project Architecture
PDF Input
   ↓
Text Extraction
   ↓
Chunking with Overlap
   ↓
Chunk-wise Summarization
   ↓
Combine Summaries
   ↓
Final Structured Summary

Tech Stack:-
Language : Python
Libraries : pypdf ollama streamlit python-dotenv
Model : Mistral (via Ollama)
Project Structure
document-summarizer/
│- app.py
│- pdf_reader.py
│- chunking.py
│- summarizer.py
│- requirements.txt
│- README.md
|- pyproject.toml

Clone the repo :- git clone https://github.com/dhruvupadhyay56/document_summarizer.git cd document_summarizer
Download and install Ollama: https://ollama.com
Pull the Mistral model : ollama pull mistral
Terminal version : python app.py
Streamlit UI version : streamlit run app.py

Created as part of an AI/LLM assignment project.
