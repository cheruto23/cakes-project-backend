from fastapi import FastAPI, Depends, HTTPException, status, Response
from schemas import CakeSchema
from sqlalchemy.orm import Session
from models import Cake
from database import get_db
app = FastAPI()

@app.get('/')
def index():
    return  {"Message": "welcome to my first api"}

@app.get('/cakes')
def cakes():
    return cakes

@app.get('/cakes/{cake_id}')
def cake(cake_id: int, db: Session = Depends(get_db)):
    cakes = db.query(Cake).filter(Cake.id == cake_id).first()
    return cakes
    

def create_cake(cake: CakeSchema, db: Session = Depends(get_db)):
    new_cake = Cake(**cake.model_dump())

    db.add(new_cake)
    db.commit()
    db.refresh(new_cake)
    return {"message": "cake created successfully", "event": new_cake}


@app.delete('/cakes/{cake_id}')
def delete_cake(cake_id: int, db: Session = Depends(get_db)):
    delete_cake = db.query(cake).filter(Cake.id == cake_id).first()

    if delete_cake == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Event {cake_id} does not exist")
    else:
        delete_cake.delete()
        db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

