from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from api.api_router import api_router


def get_application():
    _app = FastAPI()

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return _app


app = get_application()


app.include_router(api_router)
