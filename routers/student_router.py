from typing import Optional
from fastapi import APIRouter, status, HTTPException
from controllers.student_controller import StudentController
from models.student import Student, StudentResponse

router = APIRouter()


@router.get(
    "/students/{student_id}",
    response_description="Get a single student",
    response_model=Student,
    status_code=200
)
async def get_student(student_id: str):
    try:
        return StudentController.get_student(student_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get(
    "/students",
    response_description="List all students",
    response_model=StudentResponse,
    status_code=200
)
async def get_students(age: int = 0, country: str = '.'):
    try:
        students = StudentController.get_students(age, country)
        return {"data": students}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post(
    "/students",
    response_description="Add a new student",
    status_code=status.HTTP_201_CREATED
)
async def create_student(student: Student):
    try:
        student = StudentController.create_student(student.dict())
        return {"id": str(student.inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put(
    "/students/{student_id}",
    response_description="Update a student",
    status_code=204
)
async def update_student(student_id: str, update_fields: dict):
    try:
        StudentController.update_student(student_id, update_fields)
        return {}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete(
    "/students/{student_id}",
    response_description="Delete a student",
    status_code=200
)
async def delete_student(student_id: str):
    try:
        StudentController.delete_student(student_id)
        return {}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
