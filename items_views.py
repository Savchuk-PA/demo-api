from typing import Annotated

from fastapi import APIRouter, Path

router = APIRouter(prefix="/items", tags=["Items"])


@router.get("/")
def list_items():
    return {"items": [1, 2, 3, 4, 5]}


@router.get("{item_id}/")
def get_item_by_id(item_id: Annotated[int, Path(ge=1, lt=1_000_000)]):
    return {"item_id": item_id}


@router.get("/latest/")
def get_latest_item():
    return {"items": {"id": 0, "name": "latest"}}
