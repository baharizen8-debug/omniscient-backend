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
    spot_gold = 2415.80 + round(random.uniform(-0.50, 1.50), 2)
    change = "+12.40 (+0.52%)"
    
    return {
        "price": spot_gold,
        "change": change,
        "action": "LONG",
        "confidence": "78%",
        "horizon": "1-3M",
        "synopsis": "Model detects asymmetric upside skew driven by falling real yields converging with safe-haven inflows. Previous resistance at $2,400 now acting as structural support."
    }
