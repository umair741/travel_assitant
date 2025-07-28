✈️ Travel Assistant
Your AI-powered travel buddy! Plan epic trips, check weather, and discover cool places to eat, stay, or explore. Built with LangChain, FastAPI, and APIs for a seamless travel planning experience. 🌍
🌟 Features

Trip Planning: Get detailed multi-day itineraries with activities and tips.
Weather Updates: Current conditions and 5-day forecasts for your destination.
Place Finder: Discover nearby attractions, restaurants, or hotels.
Travel Q&A: Answers to visa rules, best travel times, and more!

🛠️ Tech Stack

Python + LangChain
FastAPI
Google Gemini 2.0 Flash
APIs: Geoapify, OpenWeatherMap, Tavily

📂 Project Structure

travel_assistant/
│
├── main.py           # FastAPI backend
├── agent.py          # Agent logic (not included here)
├── .gitignore
├── requirements.txt
└── README.md


🔧 Setup

Clone Repo:git clone https://github.com/yourusername/travel-assistant.git
cd travel-assistant


Virtual Env:

python -m venv venv
source venv/bin/activate 
# Windows: venv\Scripts\activate


Install Dependencies:pip install -r requirements.txt

Add API Keys:Create .env:

GEOAPIFY_API_KEY=your_key
WEATHER_API_KEY=your_key
TAVILY_API_KEY=your_key
GOOGLE_API_KEY=your_key

Get keys from Geoapify, OpenWeatherMap, Tavily, Google.

🎉 Usage

Run Server:uvicorn main:app --reload


Query API:curl -X POST http://localhost:8000/ask -H "Content-Type: application/json" -d '{"input": "Plan a 3-day trip to Paris"}'


CLI Mode:python agent.py

 Try: "Plan a 5-day trip to Skardu", "Weather in Karachi", "Restaurants in Dubai".

📋 Example
Query: "Plan a 3-day trip to Paris"Response:
Trip Plan:
- 3-Day Trip to Paris
- Weather Forecast:
  - 2025-07-29:
    - Morning: 20°C, clear
    - Afternoon: 25°C, cloudy
    - Night: 18°C, rain
- Day 1:
  - Morning: Eiffel Tower (Champ de Mars)
  - Afternoon: Louvre Museum (75001 Paris)
  - Evening: Café de Flore (172 Bd Saint-Germain)
...
Need hotel or restaurant suggestions?

🤝 Contribute

Fork the repo
Create a branch: git checkout -b feature/your-feature
Commit: git commit -m "Add feature"
Push: git push origin feature/your-feature
Open a pull request

📜 License
MIT License. See LICENSE.
💬 Contact
Open an issue or reach out at [your email/GitHub]. Happy travels! 🌴
