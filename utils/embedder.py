from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def embed_texts(texts):
    response = client.embeddings.create(
        input=texts,
        model="text-embedding-3-small"
    )
    return [r.embedding for r in response.data]

def embed_query(query):
    response = client.embeddings.create(
        input=[query],
        model="text-embedding-3-small"
    )
    return response.data[0].embedding
