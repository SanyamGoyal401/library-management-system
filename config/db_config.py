from pymongo import MongoClient
from .server_config import MONGODB_URI, DB, COLLECTION

client = MongoClient(MONGODB_URI)
db = client[DB]
collection = db[COLLECTION]
