import tiktoken

def split_text(text, max_tokens=300):
    # Use tokenizer for OpenAI embedding models
    tokenizer = tiktoken.get_encoding("cl100k_base")
    
    sentences = text.split('. ')
    chunks = []
    current_chunk = []

    for sentence in sentences:
        # Check if adding the sentence exceeds token limit
        prospective_chunk = current_chunk + [sentence]
        token_count = len(tokenizer.encode(" ".join(prospective_chunk)))

        if token_count <= max_tokens:
            current_chunk.append(sentence)
        else:
            # Save current chunk
            chunks.append(". ".join(current_chunk).strip())
            current_chunk = [sentence]

    # Add last chunk if it exists
    if current_chunk:
        chunks.append(". ".join(current_chunk).strip())

    return chunks
