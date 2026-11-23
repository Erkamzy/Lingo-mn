from app.config import settings
from fastapi import FastAPI, Depends
from sqlalchemy import text 
from sqlalchemy.orm import Session

from app.db import get_db

app = FastAPI(title=settings.app_name)

@app.get("api/health")
def health(db: Session = Depends(get_db)):
    db.execute(text("SELECT 1"))
    return {"status": "ok", "database": "ok "}