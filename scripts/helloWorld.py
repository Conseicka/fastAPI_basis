#Python
from typing import Optional

#Pydantic
from pydantic import BaseModel

#FastAPI
from fastapi import FastAPI
from fastapi import Body, Query, Path

#uvn helloWorld:app --reload
app = FastAPI()


class Location(BaseModel):
    city: str
    state: str
    country: str


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

@app.get("/person/detail")
def show_person(
    name: Optional[str] = Query(
    None,
    min_length = 1,
    max_length = 50,
    title = "Person Name",
    description = "This is the person name. It's between 1 and 50 characters."
    ),
    age: str = Query(
    ...,
    title = "Person Age.",
    description = "This is the person age. It's required."
    )

    ):
    return {name : age}

@app.get("/person/detail/{person_id}")
def show_person(
    person_id: int = Path(
    ...,
    gt = 0
        )
    ):
    return {person_id: "It exists!"}

@app.put("/person/{person_id}")
def update_person(
person_id: int = Path(
    ...,
    title = "Person ID",
    description = "This is the person ID",
    gt = 0
    ),
    person: Person = Body(...),
    location: Location = Body(...)
):
    result = person.dict()
    result.update(location.dict())
    return result
