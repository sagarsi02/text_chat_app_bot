from fastapi import FastAPI
from app.routes.chat_routes import router as chat_router

from app.services.rag_service import RAGService
from app.data.docs import DOCUMENTS

app = FastAPI()
rag_service = RAGService()

@app.on_event("startup")
async def startup_event():
    for doc in DOCUMENTS:
        await rag_service.index_document(doc)

app.include_router(chat_router)
