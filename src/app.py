from fastapi import FastAPI, HTTPException
from beanie import init_beanie
from beanie import Document
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient

MONGODB_URL = "mongodb://localhost:27017/local_db"

app = FastAPI()

class Lead(Document):
    phone_work: str
    first_name: str
    last_name: str

    class Settings:
        name = "lead"


async def connect_to_mongo():
    client = AsyncIOMotorClient(MONGODB_URL).get_default_database()
    await init_beanie(database=client, document_models=[Lead])


@app.on_event("startup")
async def startup_event():
    await connect_to_mongo()


@app.post("/lead")
async def create_lead(lead: Lead):
    lead_data = await lead.create()
    return lead_data


@app.get("/lead")
async def read_leads():
    leads = await Lead.find_many().to_list()
    return leads
