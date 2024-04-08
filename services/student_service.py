from repositories.student_repository import StudentRepository


class StudentService:
    @staticmethod
    def create_student(student_data):
        return StudentRepository.create_student(student_data)

    @staticmethod
    def get_student(student_id):
        return StudentRepository.find_student_by_id(student_id)

    @staticmethod
    def get_students(age, country):
        return StudentRepository.get_students(age, country)

    @staticmethod
    def update_student(student_id, student_data):
        return StudentRepository.update_student(student_id, student_data)

    @staticmethod
    def delete_student(student_id):
        return StudentRepository.delete_student(student_id)