import streamlit as st
from pinecone import Pinecone, ServerlessSpec

# Load Pinecone credentials from Streamlit secrets
PINECONE_API_KEY = st.secrets["PINECONE_API_KEY"]
PINECONE_ENVIRONMENT = st.secrets["PINECONE_ENVIRONMENT"]
PINECONE_INDEX_NAME = st.secrets["PINECONE_INDEX_NAME"]

# Initialize Pinecone client
pc = Pinecone(api_key=PINECONE_API_KEY)

# Set cloud and region based on environment
cloud = "aws" if "us" in PINECONE_ENVIRONMENT else "gcp"
region = PINECONE_ENVIRONMENT

# Create index if it doesn’t exist
if PINECONE_INDEX_NAME not in pc.list_indexes().names():
    pc.create_index(
        name=PINECONE_INDEX_NAME,
        dimension=1536,
        metric="cosine",
        spec=ServerlessSpec(cloud=cloud, region=region)
    )

index = pc.Index(PINECONE_INDEX_NAME)

def upsert_embeddings(chunks, embeddings):
    ids = [f"chunk-{i}" for i in range(len(chunks))]
    vectors = []
    for i in range(len(chunks)):
        vectors.append({
            "id": ids[i],
            "values": embeddings[i],
            "metadata": {"text": chunks[i]}
        })
    index.upsert(vectors=vectors)

def query_pinecone(query_vector, top_k=3):
    return index.query(vector=query_vector, top_k=top_k, include_metadata=True)
