from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def first_commit():
    return {"Hello": "World"}