# Handles FAISS vector DB - converting text to vector database

import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

embedder = SentenceTransformer('all-MiniLM-L6-v2')

def build_index(chunks):
    vectors = embedder.encode(chunks)
    dimension = vectors.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(vectors))
    return index, vectors

def query_index(index, chunks, query, top_k=3):
    query_vec = embedder.encode([query])
    distances, indices = index.search(np.array(query_vec), top_k)
    retrieved_chunks = [chunks[idx] for idx in indices[0]]
    return retrieved_chunks