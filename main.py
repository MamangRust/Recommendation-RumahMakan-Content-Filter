import random
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Initialize Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Dummy data for restaurant recommendations
restaurants = [
   {"name": "Happy Burger Joint", "location": "Jalan Bahagia No. 321", "cuisine": "Burgers", "rating": 4.8},
    {"name": "Joyful Steakhouse", "location": "Jalan Gembira No. 456", "cuisine": "Steak", "rating": 4.6},
    {"name": "Cheerful Pizzeria", "location": "Jalan Ceria No. 789", "cuisine": "Pizza", "rating": 4.4},
    {"name": "Smiling Sushi Bar", "location": "Jalan Senang No. 101", "cuisine": "Sushi", "rating": 4.9},
    {"name": "Delightful Dessert Cafe", "location": "Jalan Manis No. 202", "cuisine": "Desserts", "rating": 4.5},
    {"name": "Melancholy Cafe", "location": "Jalan Sedih No. 321", "cuisine": "Coffee", "rating": 3.8},
    {"name": "Gloomy Diner", "location": "Jalan Muram No. 456", "cuisine": "American", "rating": 3.7},
    {"name": "Bitter Bakery", "location": "Jalan Pahit No. 789", "cuisine": "Bakery", "rating": 3.5},
    {"name": "Sorrowful Sweets Shop", "location": "Jalan Sedih No. 101", "cuisine": "Sweets", "rating": 3.9},
    {"name": "Despondent Deli", "location": "Jalan Lesu No. 202", "cuisine": "Deli", "rating": 3.6}
]

# Function to recommend restaurants based on user's mood
def recommend_restaurants(mood):
    if mood == "happy":
        return [restaurant for restaurant in restaurants if restaurant["rating"] >= 4.0]
    elif mood == "sad":
        return [restaurant for restaurant in restaurants if restaurant["rating"] < 4.0]
    else:
        return random.sample(restaurants, min(len(restaurants), 3))  # Return random recommendations

# Endpoint for restaurant recommendations
@app.get("/recommend_restaurants/", response_class=HTMLResponse)
async def recommend_restaurant(request: Request, mood: str = None):
    recommended_restaurants = recommend_restaurants(mood)
    return templates.TemplateResponse("restaurant_recommendations.html", {"request": request, "recommended_restaurants": recommended_restaurants})

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
