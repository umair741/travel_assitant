import os
import requests
from dotenv import load_dotenv
from tavily import TavilyClient

# Load API keys from .env file
load_dotenv()
GEOAPIFY_API_KEY = os.getenv("GEOAPIFY_API_KEY")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

# Get coordinates from city name
def geocode_place(place_name):
    url = f"https://api.geoapify.com/v1/geocode/search?text={place_name}&apiKey={GEOAPIFY_API_KEY}"
    response = requests.get(url)
    if response.status_code != 200:
        return None, None, f"Error: {response.status_code} - {response.text}"
    
    data = response.json()
    features = data.get("features", [])
    if not features:
        return None, None, "No coordinates found."

    coords = features[0]["geometry"]["coordinates"]  # [lon, lat]
    return coords[1], coords[0], None  # lat, lon

# Get nearby places
def get_places(lat, lon, radius=5000, limit=10):
    url = (
        f"https://api.geoapify.com/v2/places?"
        f"filter=circle:{lon},{lat},{radius}"
        f"&categories=service,commercial,catering,tourism,accommodation"
        f"&limit={limit}&apiKey={GEOAPIFY_API_KEY}"
    )
    response = requests.get(url)
    if response.status_code != 200:
        return None, f"Error: {response.status_code} - {response.text}"

    data = response.json()
    places = []
    for place in data.get("features", []):
        place_info = {
            'name': place["properties"].get("name", "Unnamed Place"),
            'address': place["properties"].get("formatted", "Address not available"),
            'category': place["properties"].get("categories", ["Unknown"])[0]
        }
        places.append(place_info)
    
    return places, None

# Current weather
def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code != 200:
        return f"Error: {response.status_code} - {response.text}"

    data = response.json()
    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]
    return f"Current weather in {city}: {temp}°C with {desc}"

# 5-day forecast
def get_forecast_weather(lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code != 200:
        return {}

    data = response.json()
    forecast_list = data.get("list", [])
    daily_weather = {}

    time_labels = {
        "09:00:00": "Morning",
        "15:00:00": "Afternoon", 
        "21:00:00": "Night"
    }

    for item in forecast_list:
        dt = item.get("dt_txt", "")
        if not dt:
            continue
        date, time = dt.split()
        if time in time_labels:
            if date not in daily_weather:
                daily_weather[date] = {}
            label = time_labels[time]
            temp = item["main"]["temp"]
            desc = item["weather"][0]["description"]
            daily_weather[date][label] = f"{temp}°C with {desc}"

    return daily_weather

# Web search
def web_search(query):
    client = TavilyClient(TAVILY_API_KEY)
    result = client.search(query=query)
    if result.get("answer"):
        return f"Answer: {result['answer']}"
    results = result.get("results", [])
    if results:
        top = results[0]
        return (
            f"Top result:\n{top.get('title', 'No title')}\n"
            f"{top.get('content', 'No content')}\n"
            f"URL: {top.get('url', 'No URL')}"
        )
    return "No answer or results found."
def plan_trip(city, days=3):
    lat, lon, error = geocode_place(city)
    if error:
        return f"Could not plan trip: {error}"

    places, places_error = get_places(lat, lon, radius=15000, limit=days * 4)
    if places_error:
        return f"Could not fetch places: {places_error}"
    if not places:
        return f"No places found for {city}."

    weather_forecast = get_forecast_weather(lat, lon)
    weather_dates = list(weather_forecast.keys())

    # Start building the plan with clear structure
    plan = "Trip Plan:\n"
    plan += f"- {days}-Day Trip Plan for {city}\n"
    plan += "- Weather Forecast:\n"
    
    # Add weather forecast with proper nesting
    for i in range(min(days, len(weather_dates))):
        if i < len(weather_dates):
            date = weather_dates[i]
            plan += f"  - {date}:\n"
            weather_info = weather_forecast.get(date, {})
            for time_period in ["Morning", "Afternoon", "Night"]:
                if time_period in weather_info:
                    plan += f"    - {time_period}: {weather_info[time_period]}\n"

    # Add itinerary for each day
    places_used = 0
    time_periods = ["Morning", "Afternoon", "Evening"]
    for day in range(1, days + 1):
        plan += f"- Day {day} Itinerary:\n"
        max_today = min(3, len(places) - places_used)
        if max_today == 0:
            plan += "  - No places available. Enjoy a free day!\n"
        else:
            for i in range(max_today):
                place = places[places_used]
                time_label = time_periods[i] if i < len(time_periods) else "Later"
                plan += f"  - {time_label}: {place['name']}\n"
                plan += f"    - Address: {place['address']}\n"
                plan += f"    - Category: {place['category']}\n"
                places_used += 1
        plan += "\n"

    # Add travel tips
    plan += "- Travel Tips:\n"
    plan += "  - Check local transport in {city}\n"
    plan += "  - Book your hotel in advance\n"
    plan += "  - Try local food options\n"
    plan += "  - Watch out for weather conditions\n"

    plan += "\nWould you like me to suggest specific hotels or restaurants for this trip?"

    return plan