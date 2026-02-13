from openai import AsyncOpenAI
from app.core.config import settings

class LLMService:
    def __init__(self):
        self.client = AsyncOpenAI(
            api_key=settings.OPENAI_API_KEY
        )

    async def generate_response(self, user_message: str) -> str:
        response = await self.client.chat.completions.create(
            model=settings.MODEL_NAME,
            max_tokens=settings.MAX_TOKENS,
            messages=[
                {"role": "user", "content": user_message}
            ],
            temperature=settings.TEMPERATURE
        )

        return response.choices[0].message.content
