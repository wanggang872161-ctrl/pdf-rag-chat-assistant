🚀 PDF RAG Chat Assistant

A fully offline Retrieval-Augmented Generation (RAG) chatbot built with LangChain, FAISS, Ollama, and Gradio.

✨ Features
PDF document question answering
Fully offline local LLM inference
Vector similarity search with FAISS
Local embeddings using Ollama
ChatGPT-style interactive UI
Modular RAG pipeline

🧠 Tech Stack
Python
LangChain
FAISS
Ollama
Qwen2.5
Gradio

📂 Project Structure
.
├── app.py
├── requirements.txt
├── README.md
├── data/
│   └── test.pdf
└── rag/
    ├── loader.py
    ├── vectorstore.py
    ├── llm.py
    └── chain.py

⚡ Installation
Install dependencies
pip install -r requirements.txt
Install Ollama

Ollama Official Website

Pull models
ollama pull qwen2.5:1.5b
ollama pull nomic-embed-text
Run
python app.py

💬 Example Questions
What is self-attention?
Explain Transformer architecture.
What is vector search?
What is FAISS?

🏗️ RAG Architecture
PDF
 ↓
Chunking
 ↓
Embedding
 ↓
FAISS Vector Store
 ↓
Retriever
 ↓
Qwen2.5
 ↓
Gradio Chat UI

🚀 Future Improvements
Multi-PDF support
Streaming output
Chat memory
Docker deployment

👨‍💻 Author

wanggang872161-ctrl
