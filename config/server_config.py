from dotenv import load_dotenv
import os


load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
DB = os.getenv("DB")
COLLECTION = os.getenv("COLLECTION")
PORT=os.getenv("PORT")