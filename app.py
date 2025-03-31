from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Mount static assets
app.mount("/assets", StaticFiles(directory="assets"), name="assets")

# Serve HTML file directly
@app.get("/", response_class=FileResponse)
def home():
    return "index.html"

# python -m venv .venv
#python -m http.server 3333(port numebr)