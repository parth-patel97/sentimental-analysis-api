from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class UserInfo(BaseModel):
   name : int
   contact : int
   
class Sentence(BaseModel):
   sentence : str
   

@app.get("/hello") 
async def hello(detail:UserInfo):
    return "Hello World"
 
@app.get("/sentimental-analysis")
async def sentimental_analysis(query:Sentence):
   result = ""
   return result
 
