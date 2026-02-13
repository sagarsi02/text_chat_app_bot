from typing import Dict, List

class MemoryService:
    def __init__(self):
        # session_id → messages list
        self.store: Dict[str, List[dict]] = {}

    async def get_history(self, session_id: str) -> List[dict]:
        return self.store.get(session_id, [])

    async def save_message(self, session_id: str, role: str, content: str):
        if session_id not in self.store:
            self.store[session_id] = []

        self.store[session_id].append({
            "role": role,
            "content": content
        })
