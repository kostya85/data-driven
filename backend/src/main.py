import uvicorn
from fastapi import FastAPI, Request, Form, Depends, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse

from models.tree_classifier import TreeClassifier
from controllers.data import DataWorker

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/sample/")
async def get_sample():
    data = DataWorker()
    sample_data = data.get_sample()
    output = sample_data.to_csv(index=False)
    return StreamingResponse(
        iter([output]),
        media_type='text/csv',
        headers={"Content-Disposition": "attachment;filename=sample_data.csv"})

@app.post("/classify/")
async def predict(file: UploadFile):
    model = TreeClassifier()
    sample_data = pd.read_csv(file.file)
    return model.predict(sample_data)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=5000,
    )
