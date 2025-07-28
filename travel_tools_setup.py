from api_logic import get_places,get_weather,web_search,geocode_place,plan_trip,get_forecast_weather
from langchain.tools import Tool


def get_places_for_agent(query, radius=5000, limit=5):

    lat, lon, error = geocode_place(query)
    if error:
        return error
    return get_places(lat, lon, radius=radius, limit=limit)

def get_forecast_for_agent(city):   
    lat, lon, error = geocode_place(city)
    if error:
        return error
    return get_forecast_weather(lat, lon)


weather_tool=Tool.from_function(
    name="GetWeather", 
    func=get_weather,
    description="Get current weather for a city. Input: city name (e.g. 'Karachi')",
    return_direct=True 
)

place_tool = Tool.from_function(
    name="GetNearByPlaces",
    func=get_places_for_agent,
    description="Get nearby places for a location. Input: location name or description (e.g. 'Sukkur Ganta Ghar', 'Murree').",
    return_direct=True 
)


web_tool=Tool.from_function(
    name="websearchtool",
    func=web_search,
    description="Do a web search for any question or info.",
    return_direct=True 
)

trip_tool = Tool.from_function(
    name="MultiDayTripPlanner",
    func=plan_trip,
    description="Use this to plan detailed trips when the user asks for a 2-day, 5-day, or multi-day trip to a place. Input must include city and optionally number of days, e.g., 'Skardu 5 days' or 'Trip to Hunza for 7 days'. Returns a day-wise travel itinerary.",
    return_direct=True 
)


forecast_tool = Tool.from_function(
    name="GetForecastWeather",
    func=get_forecast_for_agent,
    description="when there is user saying give me trip plan for days give them also forcast weather in it and give combined response trip plan and weather updates of each days. Input should be a location name (e.g. 'Murree').",
    return_direct=True
)
# Export all tools as list
tools = [place_tool, weather_tool, web_tool,trip_tool,forecast_tool]


