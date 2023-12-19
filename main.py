from fastapi import FastAPI, Depends, HTTPException, status, Response
from fastapi.middleware.cors import CORSMiddleware
from schemas import CakeSchema
from sqlalchemy.orm import Session
from models import Cake
from database import get_db
app = FastAPI()

origins = ["*"]

app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                    allow_credentials=True,
                    allow_methods=["*"],
                    allow_headers=["*"],
    )

@app.post('/cakes')
def create_cake(cake: CakeSchema, db: Session = Depends(get_db)):
    new_cake = Cake(**cake.model_dump())

    db.add(new_cake)
    db.commit()
    db.refresh(new_cake)

    return {"message": "Cake created successfully", "cake": new_cake}


@app.get('/cakes')
def get_cakes(db: Session = Depends(get_db)):
    cakes = db.query(Cake).all()
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
    return {"message": "cake created successfully", "cake": new_cake}


@app.delete('/cakes/{cake_id}')
def delete_cake(cake_id: int, db: Session = Depends(get_db)):
    delete_cake = db.query(Cake).filter(Cake.id == cake_id).first()

    if not delete_cake:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Cake {cake_id} does not exist")

    db.delete(delete_cake)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

