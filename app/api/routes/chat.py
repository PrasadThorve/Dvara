from fastapi import APIRouter

from app.models.chat import ChatCompletionRequest

router = APIRouter(
    prefix="/v1", 
    tags=["Chat"]
)

@router.post("/chat/completions")
async def create_chat_completion(
    request:ChatCompletionRequest
):
    return {
        "message" : "Chat completion endpoint is working",
        "model" : request.model,
    }
