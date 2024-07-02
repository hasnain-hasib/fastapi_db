from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List, Dict


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/",response_class=HTMLResponse)
async def read_html():
    return open("static/index.html", "r").read()


class available(BaseModel):
    bengali: List[str]
    italian: List[str]
    mexican: List[str]
    japanese: List[str]
    indian: List[str]
    


food_dict = {
    'bengali': ["fish", "rice", "potato"],
    'italian': ["pasta", "pizza", "gelato"],
    'mexican': ["taco", "burrito", "quesadilla"],
    'japanese': ["sushi", "ramen", "tempura"],
    'indian': ["curry", "naan", "biryani"]
}



@app.get("/items", response_model= available)
async def food_items():
      return food_dict
  
  
@app.get("/items/{cuisine}", response_model=List[str])
async def country_food(cuisine: str):
    if cuisine not in food_dict:
        raise HTTPException(status_code=404, detail="Cuisine not found")   
    return food_dict[cuisine] 

  
  