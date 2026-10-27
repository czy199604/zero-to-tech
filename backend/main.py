from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel


app = FastAPI()

profile = {
    "heroTitle": "关于我",
    "heroSubtitle": "项目，创意，灵感，心得，我的作品",
}

class AnalyzeRequest(BaseModel):
    text: str


@app.get("/api/profile")
def get_profile():
    return JSONResponse(
        content=profile,
        media_type="application/json; charset=utf-8"
    )


@app.post("/api/analyze")
def analyze(req: AnalyzeRequest):
    data = {
        "text": req.text,
        "score": 0.5,
        "label": "偏平静",
        "pinyin": "(模块 6 再说)",
    }
    return JSONResponse(
        content=data,
        media_type="application/json; charset=utf-8"
    )