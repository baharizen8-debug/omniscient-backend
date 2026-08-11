from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Omniscient Gold API is running"}

@app.get("/api/market-data")
def get_market_data():
    spot_gold = 2415.80 + round(random.uniform(-2.00, 2.00), 2)
    change = round(random.uniform(0.10, 1.50), 2)
    
    return {
        "spot_gold": spot_gold,
        "price_change": f"+{change} (+0.52%)",
        "regime": "Stagflationary Fear"
    }
