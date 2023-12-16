from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return  {"Message": "welcome to my first api"}

@app.post('/')
def create():
    return  {"Message": "posting"}

