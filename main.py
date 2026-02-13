from fastapi import FastAPI
from app.routes.chat_routes import router as chat_router

app = FastAPI(title="Phase-1 Chatbot")

app.include_router(chat_router)