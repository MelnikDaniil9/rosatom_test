"""
Тестовое задание для ГринАтома от Даниила Мельник
приступил к выполнению 05.06.2022
подробнее см. в README.md
"""

from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def first_commit():
    return {"Hello": "World"}
