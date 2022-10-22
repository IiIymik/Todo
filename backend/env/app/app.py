from fastapi import FastAPI
from app.core.config import settings
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

@app.on_event("startup")
async def app_init():
    """
    initialize app
    """
    
    db_client = AsyncIOMotorClient(settings.MONGO_CONNECTION_STRING).fodoist
    
    await init_beanie(
        database=db_client,
        document_models=[
            
        ]
    )