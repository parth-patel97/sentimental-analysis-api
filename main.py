from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class UserInfo(BaseModel):
   name : int
   contact : int
    

@app.get("/hello")
async def hello(detail:UserInfo):
    return "Hello World"