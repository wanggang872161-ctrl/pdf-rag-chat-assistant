import requests

model_name = "qwen2.5:1.5b"   # 或 llama3

def generate_answer(context, question):

    prompt = f"""
You are a helpful assistant.

Use ONLY the context below.

If not in context, say "I don't know based on the document".

Context:
{context}

Question:
{question}

Answer:
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": model_name,
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]