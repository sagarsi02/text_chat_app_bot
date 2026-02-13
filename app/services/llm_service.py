from openai import AsyncOpenAI
from app.core.config import settings
from typing import List

class LLMService:
    def __init__(self):
        self.client = AsyncOpenAI(
            api_key=settings.OPENAI_API_KEY
        )

    async def generate_response(self, messages: List[dict]) -> str:
        response = await self.client.chat.completions.create(
            model=settings.MODEL_NAME,
            messages=messages,
            temperature=settings.TEMPERATURE,
            max_tokens=settings.MAX_TOKENS
        )

        return response.choices[0].message.content
