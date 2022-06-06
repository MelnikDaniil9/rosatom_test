"""
Тестовое задание для ГринАтома от Даниила Мельник
приступил к выполнению 05.06.2022
подробнее см. в README.md
"""

from fastapi import FastAPI


app = FastAPI()


@app.get("/frames/{request_id}/")
def get_images(request_id):
    return request_id


@app.post("/frames/")
def upload_images():
    return "successful uploaded"


@app.delete("/frames/{request_id}/")
def delete_images(request_id):
    return request_id
