from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from motor.motor_asyncio import AsyncIOMotorClient
import os

app = FastAPI()

# PostgreSQL setup
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)

async def get_db():
    async with SessionLocal() as session:
        yield session

# MongoDB setup
MONGO_URL = os.getenv("MONGO_URL")
mongo_client = AsyncIOMotorClient(MONGO_URL)
mongo_db = mongo_client["mydatabase"]

@app.get("/")
def index():
    return{"details" : "Root page"}

@app.get("/pg_data")
async def get_pg_data(db: AsyncSession = Depends(get_db)):
    result = await db.execute("SELECT now()")
    return {"timestamp": result.scalar()}

@app.get("/mongo_data")
async def get_mongo_data():
    data = await mongo_db["mycollection"].find_one()
    return data or {"message": "No data found"}
