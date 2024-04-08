from bson import ObjectId
from pymongo import ReturnDocument

from config.db_config import collection


class StudentRepository:
    @staticmethod
    def get_students(age, country):
        return collection.find({"age": {"$gte": age}, "address.country": {"$regex": country}}, {"address": 0})

    @staticmethod
    def create_student(student_data):
        return collection.insert_one(student_data)

    @staticmethod
    def find_student_by_id(student_id):
        return collection.find_one({"_id": ObjectId(student_id)})

    @staticmethod
    def update_student(student_id, student_data):
        return collection.find_one_and_update({"_id": ObjectId(student_id)}, {"$set": student_data}, return_document=ReturnDocument.AFTER)

    @staticmethod
    def delete_student(student_id):
        return collection.delete_one({"_id": ObjectId(student_id)})
