from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.student_router import router as student_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def health_check():
    return {"Message": "System is healthy and running!"}


app.include_router(student_router)
