
from fastapi import FastAPI

app = FastAPI()

@app.get('/',tags=["Root"])
def home():
    return {'msg': 'Welcome in my api'}