from fastapi import FastAPI

from app.api.routes.chat import router as chat_router

app = FastAPI(
    title="Dvara",
    description="Open-source AI API Gateway for routing, securing, and observing LLM requests",
    version="0.1.0",
)

app.include_router(chat_router)

@app.get("/health")
async def health_check():
    return {"status": "healthy"}


