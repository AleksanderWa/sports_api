from fastapi import FastAPI

from db.config import engine
from db.models import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Fast Sports API",
    description="Football, NBA, and many more API",
    version="0.0.1"
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
