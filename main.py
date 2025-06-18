from utils.pdf_loader import extract_resume_text
from utils.text_splitter import split_text
from utils.embedder import embed_texts, embed_query
from utils.pinecone_store import upsert_embeddings, query_pinecone
from config import OPENAI_API_KEY
import openai

# STEP 1: Extract resume text from the PDF
resume_text = extract_resume_text("resume.pdf")
print("✅ Resume text extracted.")

# STEP 2: Chunk the text
chunks = split_text(resume_text)
print(f"✅ Split into {len(chunks)} chunks.")

# STEP 3: Embed and upsert into Pinecone
embeddings = embed_texts(chunks)
upsert_embeddings(chunks, embeddings)
print("✅ Embeddings upserted to Pinecone.")

# STEP 4: Ask your question
question = "What technical skills do I have?"
query_vector = embed_query(question)
results = query_pinecone(query_vector)

# STEP 5: Build context from top matches
context = "\n".join([match["metadata"]["text"] for match in results["matches"]])
prompt = f"Context:\n{context}\n\nQuestion: {question}\nAnswer:"

# STEP 6: Send prompt to GPT
from openai import OpenAI
client = OpenAI(api_key=OPENAI_API_KEY)

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": prompt}],
    temperature=0
)


# STEP 7: Show answer
answer = response.choices[0].message.content
print("\n🤖 Answer:\n", answer)