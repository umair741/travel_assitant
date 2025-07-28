✈️ Travel Assistant
Welcome to Travel Assistant! Your AI-powered buddy for planning epic trips, checking weather, and finding the best spots to eat, stay, or explore. Built with LangChain, FastAPI, and APIs like Geoapify and OpenWeatherMap, this tool makes travel planning a breeze. 🌍
🚀 What Can It Do?

Plan Multi-Day Trips: Get detailed itineraries for any destination, complete with activities and tips.
Check Weather: Current conditions and 5-day forecasts to keep your plans on track.
Discover Places: Find nearby attractions, restaurants, or hotels with addresses and details.
Answer Travel Questions: From visa info to the best time to visit, we've got you covered!

🛠️ Tech Stack

Python + LangChain for smart AI logic
FastAPI for a snappy API
Google Gemini 2.0 Flash for chatty responses
APIs: Geoapify (locations), OpenWeatherMap (weather), Tavily (web search)

📂 Project Structure
travel-assistant/
├── agent.py              # Sets up the AI agent
├── api_logic.py         # Handles API calls
├── travel_tools_setup.py # Defines cool tools
├── main.py              # FastAPI server
├── .env                 # Your API keys (keep it secret!)
├── requirements.txt     # Dependencies
└── README.md            # You're reading it!

🔧 Setup

Clone the Repo:
git clone https://github.com/yourusername/travel-assistant.git
cd travel-assistant


Virtual Environment:
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate


Install Dependencies:
pip install -r requirements.txt


Add API Keys:Create a .env file:
GEOAPIFY_API_KEY=your_key
WEATHER_API_KEY=your_key
TAVILY_API_KEY=your_key
GOOGLE_API_KEY=your_key

Get keys from Geoapify, OpenWeatherMap, Tavily, and Google.


🎉 Try It Out!

Start the Server:
uvicorn main:app --reload


Ask Away:Hit the API at http://localhost:8000/ask:
curl -X POST http://localhost:8000/ask -H "Content-Type: application/json" -d '{"input": "Plan a 3-day trip to Paris"}'

Or run agent.py for a CLI chat:
python agent.py

Try queries like:

"Plan a 5-day trip to Skardu"
"Weather in Karachi"
"Best restaurants in Dubai"



🌟 Example Output
Query: "Plan a 3-day trip to Paris"
Response:
Trip Plan:
- 3-Day Trip to Paris
- Weather Forecast:
  - 2025-07-29:
    - Morning: 20°C, clear skies
    - Afternoon: 25°C, partly cloudy
    - Night: 18°C, light rain
- Day 1 Itinerary:
  - Morning: Eiffel Tower
    - Address: Champ de Mars, Paris
    - Category: Tourism
  - Afternoon: Louvre Museum
    - Address: 75001 Paris
    - Category: Tourism
  - Evening: Café de Flore
    - Address: 172 Bd Saint-Germain
    - Category: Catering
...
Want restaurant or hotel tips for Paris?

🤝 Contribute
Got ideas? Fork the repo, make a branch, and send a pull request! Let's make travel planning even cooler.
📜 License
MIT License. See LICENSE for details.
💬 Questions?
Open an issue or ping me at umics38@gmail.com. Happy travels! 🌴
