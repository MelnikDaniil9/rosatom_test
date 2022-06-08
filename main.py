"""
Тестовое задание для ГринАтома от Даниила Мельник
приступил к выполнению 05.06.2022
подробнее см. в README.md
"""
import uuid
from typing import List
from fastapi import FastAPI, status, File, HTTPException, UploadFile
from databases import Database

database = Database("postgresql+asyncpg://postgres:postgrespw@localhost:49153/postgres")

app = FastAPI()


@database.transaction()
async def select_images():
    result = await database.fetch_all("SELECT now() as now")
    return result


@database.transaction()
async def create_inbox():
    create_inbox_sql = """
        create table if not exists inbox (
          id serial,
          request_uuid varchar(36),
          image_name varchar(40),
          created_time timestamp default now()
        );
        """
    await database.execute(create_inbox_sql)


@app.on_event("startup")
async def startup():
    await database.connect()
    await create_inbox()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/frames/{request_uuid}/")
async def get_images(request_uuid: str):
    select_images_sql = f"""
    select image_name, created_time
    from inbox
    where request_uuid = :request_uuid;
    """
    rows = await database.fetch_all(
        select_images_sql, values={'request_uuid': request_uuid}
    )
    response = []
    for row in rows:
        item = {
            "image_name": row.image_name,
            "created_time": row.created_time.strftime("%Y-%m-%d %H:%M"),
        }
        response.append(item)
    return response


@app.post("/frames/")
async def upload_images(images: List[UploadFile] = File(...)):
    """
 :param images: список изображений в байтовом формате
 :return:
    """
    if not (0 < len(images) < 16):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Необходимо от 1 до 15 изображений",
        )
    images_ = []
    for i, image in enumerate(images, start=1):
        if image.content_type != "image/jpeg":
            raise HTTPException(
                status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
                detail=f"Неверный формат {i} изображения {image.content_type}"
            )
        images_.append((f'{uuid.uuid4()}.jpg', image))
    request_uuid = str(uuid.uuid4())
    # TODO generate images name as uuid4() + '.jpg'
    # TODO insert into database
    # TODO await insert_into_inbox(request_uuid, images_)
    # TODO insert images into min.io

    return ['uuid1.jpg', 'uuid2.jpg']


@app.delete("/frames/{request_id}/")
async def delete_images(request_id):
    return request_id
