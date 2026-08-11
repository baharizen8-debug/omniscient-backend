from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import random

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="."), name="static")

@app.get("/")
async def read_index():
    return FileResponse('index.html')

@app.get("/api/gold-data")
def get_gold_data():
    spot_gold = 2415.80 + round(random.uniform(0.10, 1.50), 2)
    statuses = ["Bullish", "Bearish", "Stagflationary Fear"]
    current_status = random.choice(statuses)
    
    return {
        "price": spot_gold,
        "status": current_status
    }
