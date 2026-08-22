from fastapi import FastAPI

app = FastAPI(
    title="Dvara",
    description="Open-source AI API Gateway for routing, securing, and observing LLM requests",
    version="0.1.0",
)

@app.get("/health")
async def health_check():
    return {
        "status":"healthy"
    }