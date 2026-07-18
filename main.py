from fastapi import FastAPI
from api import customers

app = FastAPI(
    title="BouwAI API",
    description="AI assistent voor de Belgische bouwsector",
    version="0.1"
)


app.include_router(
    customers.router
)


@app.get("/")
def home():
    return {
        "status": "online",
        "message": "Welkom bij BouwAI"
    }
