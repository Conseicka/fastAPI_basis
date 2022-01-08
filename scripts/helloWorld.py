#Python
from typing import Optional

#Pydantic
from pydantic import BaseModel

#FastAPI
from fastapi import FastAPI
from fastapi import Body

#uvn helloWorld:app --reload

app = FastAPI()

#Models

class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    hair_color: Optional[str] = None
    is_married: Optional[bool] = None



@app.get("/")
def home():
    return{"hello": "world"}

#Request and Response body

@app.post("/persona/new")
def create_preson(person: Person = Body(...)):
    return person
