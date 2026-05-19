from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter

def load_pdf(path):
    loader = PyPDFLoader(path)
    documents = loader.load()

    splitter = CharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    docs = splitter.split_documents(documents)
    return docs