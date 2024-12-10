from fastapi import FastAPI
from db import models
from router import user, article
from db.database import engine
app = FastAPI()
app.include_router(user.router)
app.include_router(article.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}

models.Base.metadata.create_all(engine)