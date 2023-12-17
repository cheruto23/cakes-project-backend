from fastapi import FastAPI
from schemas import CakeSchema
app = FastAPI()

@app.get('/')
def index():
    return  {"Message": "welcome to my first api"}

@app.get('/cakes')
def cakes():
    return []

@app.get('/cakes/{cake_id}')
def cake():
    return []

@app.post('/cakes')
def create_cake(cakes : CakeSchema):
    print(cakes)
    return  {"Message": "posting"}

@app.patch('/cakes/{cake_id}')
def update_cake(cake_id: int):
    return  {"Message":f"cakes {cake_id} created succeesfully"}

@app.delete('/cakes/{cake_id}')
def delete_cake(cake_id: int):
    return  {"Message":f"cakes {cake_id} deleted succeesfully"}

