import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/service/info")
async def root():
    return {"message": "这是一个python api"}

if __name__ == "__main__":
    uvicorn.run(app='fastapi_test:app', host="0.0.0.0", port=8100, reload=True, debug=True)
