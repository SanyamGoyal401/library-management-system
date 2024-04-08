from pydantic import BaseModel
from typing import List


class Student(BaseModel):

    class Address(BaseModel):
        city: str
        country: str

    name: str
    age: int
    address: Address


class StudentResponse(BaseModel):

    class Student(BaseModel):
        name: str
        age: int

    data: List[Student]
