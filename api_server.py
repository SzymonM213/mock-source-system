from fastapi import FastAPI

from dinosaurs import generate_dinosaur

app = FastAPI()

records = [generate_dinosaur() for _ in range(1001)]

@app.get("/dinosaurs")
async def get_dinosaurs():
    return records