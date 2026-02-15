from app.services.embedding_service import EmbeddingService
from app.services.vector_store_service import VectorStoreService
from typing import List

class RAGService:
    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.vector_store = VectorStoreService()

    async def index_document(self, text: str):
        embedding = await self.embedding_service.generate_embedding(text)
        await self.vector_store.add_vector(embedding, text)

    async def retrieve(self, query: str) -> List[str]:
        query_embedding = await self.embedding_service.generate_embedding(query)
        results = await self.vector_store.similarity_search(query_embedding)
        return results
