from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OllamaEmbeddings

def create_vectorstore(docs):

    # ✔ 完全离线 embedding
    embeddings = OllamaEmbeddings(
        model="nomic-embed-text"
    )

    db = FAISS.from_documents(docs, embeddings)
    return db