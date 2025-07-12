import os
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import FileResponse, JSONResponse


app = FastAPI()

# Define path to your static files directory
STATIC_DIR = os.getenv("DOWNLOADER_STATIC_DIR", "static")
if not os.path.exists(STATIC_DIR):
    os.mkdir(STATIC_DIR)


class FileInfo(BaseModel):
    name: str
    size: int  # in bytes


@app.get("/download/{filename}", response_model=None)
def download_file(filename: str) -> Union[JSONResponse, FileResponse]:
    file_path = os.path.join(STATIC_DIR, filename)

    if not os.path.exists(file_path):
        return JSONResponse({"error": "File not found"}, status_code=404)

    return FileResponse(
        path=file_path,
        filename=filename,
        media_type='application/octet-stream'
    )



@app.get("/files", response_model=list[FileInfo])
def list_files() -> list[dict]:
    files_info = []
    for f in os.listdir(STATIC_DIR):
        full_path = os.path.join(STATIC_DIR, f)
        if os.path.isfile(full_path):
            files_info.append({
                "name": f,
                "size": os.path.getsize(full_path)  # Size in bytes
            })
    return files_info
