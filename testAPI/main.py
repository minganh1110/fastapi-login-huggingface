from fastapi import FastAPI,File,UploadFile
import uvicorn
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



users_data = [
    {"id": 1, "name": "John", "age": 20, "email": "john@example.com"},
    {"id": 2, "name": "Jane", "age": 21, "email": "jane@example.com"}
]

@app.get("/")
async def root():
    return {"users": users_data}

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    for user in users_data:
        if user["id"] == user_id:
            return {"user": user}
    return {"error": "User not found"}

@app.put("/users/{user_id}")
async def update_user(user_id: int, name: str):
    for user in users_data:
        if user["id"] == user_id:
            user["name"] = name  # Thay đổi thực sự
            return {"message": "Updated successfully", "user": user}
    return {"error": "User not found"}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename}
