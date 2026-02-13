from fastapi import APIRouter
from app.schemas.chat_schema import ChatRequest, ChatResponse
from app.services.llm_service import LLMService
from app.services.memory_service import MemoryService

router = APIRouter()

llm_service = LLMService()
memory_service = MemoryService()

@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):

    # 1️⃣ Get previous history
    history = await memory_service.get_history(request.session_id)

    # 2️⃣ Add current user message
    history.append({
        "role": "user",
        "content": request.message
    })

    # 3️⃣ Generate response using full conversation
    reply = await llm_service.generate_response(history)

    # 4️⃣ Save assistant reply
    await memory_service.save_message(
        request.session_id,
        "assistant",
        reply
    )

    return ChatResponse(reply=reply)
