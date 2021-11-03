from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello John"}


@app.get("/posts")
def get_posts():
    return {"data": "This is your post"}
