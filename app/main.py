from app.config import settings
from fastapi import FastAPI

app = FastAPI(title=settings.app_name)

@app.get("/api/health")
def health():
    return {'status ':'ok'}

@app.get("/api/hello/{name}")
def hello(name: str):
    return {"message": f"Сайн уу, {name}!"}