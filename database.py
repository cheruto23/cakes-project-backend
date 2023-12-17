from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgres://cakes_j0q4_user:zQexdocpEsV8yW3PWWjVRQ4qujzVOAXa@dpg-clv2kqug1b2c73cd21kg-a.frankfurt-postgres.render.com/cakes_j0q4")

SessionLocal = sessionmaker(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()