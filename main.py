from fastapi import FastAPI

app = FastAPI(
    title="BouwAI API",
    description="AI assistent voor de Belgische bouwsector",
    version="0.1"
)

@app.get("/")
def home():
    return {
        "status": "online",
        "message": "Welkom bij BouwAI"
    }
