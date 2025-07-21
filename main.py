from contextlib import asynccontextmanager

import uvicorn
from typing import Annotated
from fastapi import FastAPI, Body, Path
from pydantic import EmailStr, BaseModel
from items_views import router as items_router
from users.views import roter as users_router
from api_v1 import router as router_v1
from core.settings import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(items_router)
app.include_router(users_router)
app.include_router(router_v1, prefix=settings.api_v1_prefix)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
