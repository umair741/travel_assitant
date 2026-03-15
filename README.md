# ✈️ AI Travel Assistant

An intelligent travel assistant powered by **Google Gemini**, **LangChain ReAct Agent**, and **FastAPI**. The agent autonomously decides which tools to use based on user queries — planning trips, fetching real-time weather, finding nearby places, and searching the web.

---

## 🧠 How It Works

This project uses a **ReAct (Reasoning + Acting) Agent** pattern:

1. User sends a query
2. Gemini LLM **reasons** about what needs to be done
3. Agent **selects the right tool** automatically
4. Tool fetches real data from APIs
5. Gemini **formats** the response and returns it to the user

```
User Query
    ↓
Gemini LLM (Reasoning)
    ↓
Tool Selection (automatic)
    ↓
Real API Data (Weather / Places / Web)
    ↓
Formatted Response
```

---

## 🚀 Features

- 🗺️ **Multi-day Trip Planning** — day-wise itinerary with real places
- 🌤️ **Real-time Weather** — current weather + 5-day forecast
- 📍 **Nearby Places** — hotels, restaurants, tourist attractions
- 🔍 **Web Search** — general travel info, visa, tips
- 🤖 **ReAct Agent** — autonomous tool calling with LangChain

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| LLM | Google Gemini (`gemini-3-flash-preview`) |
| Agent Framework | LangChain ReAct Agent |
| Backend | FastAPI + Uvicorn |
| Weather | OpenWeatherMap API |
| Places & Geocoding | Geoapify API |
| Web Search | Tavily API |

---

## ⚙️ Setup

### 1. Clone the repo
```bash
git clone https://github.com/your-username/travel-assistant.git
cd travel-assistant
```

### 2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate       # Windows
source venv/bin/activate    # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Create `.env` file
```env
GOOGLE_API_KEY=your_gemini_api_key
WEATHER_API_KEY=your_openweathermap_key
GEOAPIFY_API_KEY=your_geoapify_key
TAVILY_API_KEY=your_tavily_key
```

### 5. Run the server
```bash
uvicorn app:app --reload
```

### 6. Test via Swagger UI
```
http://127.0.0.1:8000/docs
```

---

## 🔑 API Keys

| API | Free Tier | Link |
|-----|-----------|------|
| Google Gemini | 20 req/day | [aistudio.google.com](https://aistudio.google.com) |
| OpenWeatherMap | 1000 req/day | [openweathermap.org](https://openweathermap.org) |
| Geoapify | 3000 req/day | [geoapify.com](https://geoapify.com) |
| Tavily | 1000 req/month | [tavily.com](https://tavily.com) |

---

## 📁 Project Structure

```
travel_assistant/
├── app.py                  # FastAPI server & API endpoints
├── agent.py                # LangChain ReAct Agent + Gemini LLM
├── api_logic.py            # Core logic: Weather, Places, Trip Planning
├── travel_tools_setup.py   # LangChain Tool definitions
├── requirements.txt        # Python dependencies
└── .env                    # API keys (not committed)
```

---

## 🛠️ LangChain Tools

| Tool | Description |
|------|-------------|
| `MultiDayTripPlanner` | Plans day-wise trip itinerary with weather |
| `GetWeather` | Current weather for any city |
| `GetForecastWeather` | 5-day weather forecast |
| `GetNearByPlaces` | Nearby hotels, restaurants, tourist spots |
| `WebSearchTool` | General travel info via web search |

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/ask` | Send query to the travel agent |
| GET | `/docs` | Swagger UI |

### Request
```json
{
  "input": "Plan a 5 day trip to Lahore"
}
```

### Response
```json
{
  "response": "Here is your 5-day Lahore trip plan..."
}
```

---

## 💬 Example Queries

- `"Plan a 5 day trip to Lahore"`
- `"What is the weather in Karachi?"`
- `"Find nearby restaurants in Murree"`
- `"Best time to visit Hunza Valley"`
- `"Visa requirements for Pakistani citizens to Turkey"`

---

## 👨‍💻 Author

Built with ❤️ using **LangChain + Google Gemini + FastAPI**