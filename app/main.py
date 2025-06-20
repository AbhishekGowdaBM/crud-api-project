from fastapi import FastAPI
from .db import Base, engine
from .routers import items

Base.metadata.create_all(bind=engine)

app = FastAPI(title="CRUD API with FastAPI + SQLite")

app.include_router(items.router)
