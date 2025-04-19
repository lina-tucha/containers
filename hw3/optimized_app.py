from fastapi import FastAPI
import platform

app = FastAPI()

@app.get("/")
async def root():
    return {
        "message": "Hello from container!",
        "system": platform.system(),
        "container_size": "Under 100MB!"
    }