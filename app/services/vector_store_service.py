import numpy as np
from typing import List, Dict

class VectorStoreService:
    def __init__(self):
        self.vectors: List[Dict] = []

    async def add_vector(self, embedding: List[float], text: str):
        self.vectors.append({
            "embedding": np.array(embedding),
            "text": text
        })

    async def similarity_search(self, query_embedding: List[float], top_k: int = 3):
        query_vector = np.array(query_embedding)

        scores = []
        for item in self.vectors:
            score = np.dot(query_vector, item["embedding"])
            scores.append((score, item["text"]))

        scores.sort(reverse=True, key=lambda x: x[0])

        return [text for _, text in scores[:top_k]]
