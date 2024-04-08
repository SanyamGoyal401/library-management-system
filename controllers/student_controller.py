from fastapi import HTTPException
from services.student_service import StudentService


class StudentController:
    @staticmethod
    def create_student(student_data):
        return StudentService.create_student(student_data)

    @staticmethod
    def get_student(student_id):
        student = StudentService.get_student(student_id)
        if not student:
            raise HTTPException(status_code=404, detail="Student not found with this id")
        return student

    @staticmethod
    def get_students(age, country):
        return StudentService.get_students(age, country)

    @staticmethod
    def update_student(student_id, student_data):
        student = StudentService.get_student(student_id)
        if not student:
            raise HTTPException(status_code=404, detail="Student not found with this id")
        return StudentService.update_student(student_id, student_data)

    @staticmethod
    def delete_student(student_id):
        student = StudentService.get_student(student_id)
        if not student:
            raise HTTPException(status_code=404, detail="Student not found with this id")
        return StudentService.delete_student(student_id)