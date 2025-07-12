import os
import uvicorn


if __name__ == "__main__":
    uvicorn.run(
        app='main:app',
        host=os.getenv('DOWNLOADER_HOST', '0.0.0.0'),
        port=int(os.getenv('DOWNLOADER_PORT', 8000)),
        workers=int(os.getenv('DOWNLOADER_WORKERS_COUNT', 2)),
        reload=bool(os.getenv('DOWNLOADER_DEBUG', True)),
        lifespan="off",
    )
