from transformers import pipeline
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()

# Tạo pipeline phân loại cảm xúc sử dụng mô hình đã fine-tune từ DistilBERT
classifier = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

# Dữ liệu user giả lập
valid_user = {
    "username": "admin",
    "password": "123456"
}

# Model cho dữ liệu đầu vào
class LoginRequest(BaseModel):
    username: str
    password: str
    text: str


@app.post("/analyze")
async def analyze_sentiment(request: LoginRequest):
    if request.username != valid_user["username"] or request.password != valid_user["password"]:
        raise HTTPException(status_code=401, detail="Sai tên đăng nhập hoặc mật khẩu")

    result = classifier(request.text)[0]  # ví dụ: {'label': 'POSITIVE', 'score': 0.999...}
    return {
        "message": "Đăng nhập thành công!",
        "analysis_result": {
            "label": result["label"],
            "confidence": round(result["score"], 4)
        }
    }

