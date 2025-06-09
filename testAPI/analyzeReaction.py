from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

model = pipeline("sentiment-analysis",model="nlptown/bert-base-multilingual-uncased-sentiment")

class Reaction(BaseModel):
    reaction: str

@app.get("/")
async def root():
    return {"message": "Hello eveyone"}

@app.post("/analyzeReaction/")
async def analyzeReaction(reaction: Reaction):
    result = model(reaction.reaction)
    return {"label": result[0]['label'], "score": result[0]['score']}