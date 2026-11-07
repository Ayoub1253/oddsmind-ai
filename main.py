from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="ODDSMIND AI API", version="0.1.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=False,
                   allow_methods=["GET", "POST"], allow_headers=["*"])

@app.get("/health")
def health():
    return {"status": "ok", "mode": "starter"}

@app.get("/api/sports")
def sports():
    return {"sports": ["football", "basketball", "tennis", "hockey", "baseball"]}

@app.post("/api/analyze")
def analyze(payload: dict):
    return {"status": "not_configured",
            "message": "Connect verified sports data and AI providers before live analysis.",
            "received": payload}
