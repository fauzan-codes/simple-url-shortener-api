#  app\main.py

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse
# from fastapi import HTTPException

from app.database import engine, Base, SessionLocal
from app import models
from app.schemas import URLCreate
from app.utils import generate_short_code

import re

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "API jalan!"}



@app.post("/shorten")
def create_short_url(data: URLCreate, db: Session = Depends(get_db)):

    if data.custom_code:

        if not re.match("^[a-zA-Z0-9_-]+$", data.custom_code):
            raise HTTPException(
                status_code=400,
                detail="Custom code only allows letters, numbers, - and _"
            )

        existing = db.query(models.URL).filter(
            models.URL.short_code == data.custom_code
        ).first()

        if existing:
            raise HTTPException(
                status_code=400,
                detail="Custom URL already taken"
            )

        short_code = data.custom_code

    else:
        short_code = generate_short_code()

    new_url = models.URL(
        original_url=data.url,
        short_code=short_code
    )

    db.add(new_url)
    db.commit()
    db.refresh(new_url)

    return {"short_url": short_code}



@app.get("/{code}")
def redirect_url(code: str, db: Session = Depends(get_db)):
    url = db.query(models.URL).filter(models.URL.short_code == code).first()

    if not url:
        raise HTTPException(status_code=404, detail="URL not found")
    
    url.clicks += 1
    db.commit()

    return RedirectResponse(url.original_url)