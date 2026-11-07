# ODDSMIND AI Starter
Prototype starter for a multi-sport analysis website.

IMPORTANT: The frontend contains demo fixtures only. No live sports feed, odds source, AI provider, betting account, or payments are connected. Do not treat demo content as real predictions. Keep all API keys on the backend.

## Files
- frontend/index.html: responsive demo interface
- backend/main.py: FastAPI starter API
- backend/requirements.txt: dependencies
- backend/.env.example: provider-key placeholders

## Run backend on Windows
cd backend
python -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt
uvicorn main:app --reload

Then open http://127.0.0.1:8000/health
