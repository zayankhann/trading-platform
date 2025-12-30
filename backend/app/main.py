from fastapi import FastAPI
from app.api.routes.settings import router as settings_router

app = FastAPI(title="Systematic Trading Operations Platform")

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(settings_router, tags=["settings"])
