from fastapi import FastAPI
from app.routes.matches import router as matches_router
from app.routes.leagues import router as leagues_router

app = FastAPI(title="FootyStats Aggregator API")

app.include_router(matches_router, prefix="/matches", tags=["matches"])
app.include_router(leagues_router, prefix="/leagues", tags=["leagues"])

@app.get("/")
def root():
    return {"status":"running"}
