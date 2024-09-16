from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.responses import HTMLResponse
import os

app = FastAPI()

# Mount the static directory to serve static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Serve the index.html file
@app.get("/", response_class=HTMLResponse)
async def read_index():
    file_path = os.path.join("app", "static", "index.html")
    with open(file_path) as f:
        return f.read()


