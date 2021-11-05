from pydantic import BaseModel

class PassParam(BaseModel):
    numbers:int
    length:int

