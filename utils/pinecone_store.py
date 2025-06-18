import os
from pinecone import Pinecone, ServerlessSpec
from config import PINECONE_API_KEY, PINECONE_ENVIRONMENT, PINECONE_INDEX_NAME

# Create Pinecone client
pc = Pinecone(api_key=PINECONE_API_KEY)

# Extract region and cloud from environment string
cloud = "aws" if "us" in PINECONE_ENVIRONMENT else "gcp"
region = PINECONE_ENVIRONMENT

# Create index if it doesn't exist
if PINECONE_INDEX_NAME not in pc.list_indexes().names():
    pc.create_index(
        name=PINECONE_INDEX_NAME,
        dimension=1536,
        metric="cosine",
        spec=ServerlessSpec(cloud=cloud, region=region)
    )

# Get the index object
index = pc.Index(PINECONE_INDEX_NAME)

# Function to upsert embeddings
def upsert_embeddings(chunks, embeddings):
    vectors = []
    for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
        vectors.append({
            "id": f"chunk-{i}",
            "values": embedding,
            "metadata": {"text": chunk}
        })
    index.upsert(vectors=vectors)

# Function to query Pinecone
def query_pinecone(query_vector, top_k=3):
    return index.query(
        vector=query_vector,
        top_k=top_k,
        include_metadata=True
    )
