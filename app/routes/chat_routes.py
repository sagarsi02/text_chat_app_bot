from fastapi import APIRouter
from app.schemas.chat_schema import ChatRequest, ChatResponse
from app.services.llm_service import LLMService

router = APIRouter()
llm_service = LLMService()

@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    reply = await llm_service.generate_response(request.message)
    return ChatResponse(reply=reply)
