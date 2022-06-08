"""
Тестовое задание для ГринАтома от Даниила Мельник
приступил к выполнению 05.06.2022
подробнее см. в README.md
"""
from typing import List

from fastapi import FastAPI, Request, status, File, HTTPException
from databases import Database

database = Database("postgresql+asyncpg://postgres:postgrespw@localhost:49153/postgres")

app = FastAPI()


@database.transaction()
async def select_images():
    result = await database.fetch_all("SELECT now() as now")
    return result


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/frames/{request_id}/")
async def get_images(request_id):
    return request_id


@app.post("/frames/")
async def upload_images(images: List[bytes] = File()):
    """
 :param images: список изображений в байтовом формате
 :return:
    """
    if not (0 < len(images) < 16):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Необходимо от 1 до 15 изображений",
        )
    return {"file_sizes": [len(image) for image in images]}


@app.delete("/frames/{request_id}/")
async def delete_images(request_id):
    return request_id
