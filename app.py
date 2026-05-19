import gradio as gr

from rag.loader import load_pdf
from rag.vectorstore import create_vectorstore
from rag.llm import generate_answer
from rag.chain import retrieve_answer

docs = load_pdf("data/test.pdf")
db = create_vectorstore(docs)

def chat(message, history):

    if not message.strip():
        return ""

    answer = retrieve_answer(db, generate_answer, message)
    return answer

demo = gr.ChatInterface(fn=chat)
demo.launch()