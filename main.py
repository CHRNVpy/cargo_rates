import uvicorn
from fastapi import FastAPI
from typing import Dict, AnyStr, List
from models import CargoRate, save_rates_to_db, get_rate

app = FastAPI()


@app.post("/api/rates")
async def upload_rates(data: Dict[AnyStr, List]):
    await save_rates_to_db(data)
    return {"message": "Rates uploaded successfully"}


@app.get("/api/get_rates")
async def upload_rates(data: Dict):
    value = next(iter(data.values()))["value"]
    rate = await get_rate(data)
    return {"Insurance_cost": float(value) * float(rate)}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)

