from pydantic import BaseModel

class CakeSchema(BaseModel):
    category : str
    flavor : str
    price : int
    imageUrl : str