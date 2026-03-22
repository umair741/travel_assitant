---
title: Travel Assistant
emoji: ✈️
colorFrom: blue
colorTo: green
sdk: docker
pinned: false
---

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
    ↓
LangSmith Tracing (tokens, latency, cost)
```

---

## 🚀 Features

- 🗺️ **Multi-day Trip Planning** — day-wise itinerary with real places
- 🌤️ **Real-time Weather** — current weather + 5-day forecast
- 📍 **Nearby Places** — hotels, restaurants, tourist attractions
- 🔍 **Web Search** — general travel info, visa, tips
- 🤖 **ReAct Agent** — autonomous tool calling with LangChain
- 🧠 **Conversation Memory** — agent remembers previous messages in a session
- 📊 **LangSmith Tracing** — token usage, latency, cost monitoring
- 🐳 **Docker Support** — containerized for easy deployment

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| LLM | Google Gemini (`gemini-3-flash-preview`) |
| Agent Framework | LangChain ReAct Agent |
| Memory | LangChain `ConversationSummaryBufferMemory` |
| Backend | FastAPI + Uvicorn |
| Weather | OpenWeatherMap API |
| Places & Geocoding | Geoapify API |
| Web Search | Tavily API |
| Observability | LangSmith |
| Containerization | Docker |

---

## 🧠 Conversation Memory

This project uses **`ConversationSummaryBufferMemory`** from LangChain to give the agent memory during a session.

### How it works
```
User: "Plan a 5 day trip to Lahore"
    ↓ saved in memory
User: "What was the first day activity?"
    ↓ agent remembers previous response ✅
```

### Memory Type
| Type | Description |
|------|-------------|
| `ConversationSummaryBufferMemory` | Keeps recent messages + summarizes older ones automatically |

### Key Settings
| Setting | Value | Description |
|---------|-------|-------------|
| `memory_key` | `chat_history` | Key used in prompt |
| `return_messages` | `True` | Returns message objects |
| `max_token_limit` | `2000` | Summarizes after 2000 tokens |

> Note: Memory is session-based — it resets when the server restarts.

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

# LangSmith (Observability)
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=your_langsmith_api_key
LANGCHAIN_PROJECT=default
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

## 🐳 Docker Setup

### 1. Build the image
```bash
docker build -t travel-assistant .
```

### 2. Run the container
```bash
docker run --env-file .env -p 8000:8000 travel-assistant
```

### 3. Test via Swagger UI
```
http://localhost:8000/docs
```

---

## 🔑 API Keys

| API | Free Tier | Link |
|-----|-----------|------|
| Google Gemini | 20 req/day | [aistudio.google.com](https://aistudio.google.com) |
| OpenWeatherMap | 1000 req/day | [openweathermap.org](https://openweathermap.org) |
| Geoapify | 3000 req/day | [geoapify.com](https://geoapify.com) |
| Tavily | 1000 req/month | [tavily.com](https://tavily.com) |
| LangSmith | 5000 traces/month | [smith.langchain.com](https://smith.langchain.com) |

---

## 📊 LangSmith Observability

This project uses **LangSmith** to monitor and trace all agent activity in real-time.

### What is tracked?
| Metric | Description |
|--------|-------------|
| 🪙 Token Usage | Input/output tokens per request |
| ⏱️ Latency | How long each tool/API call takes |
| 💰 Cost | Estimated cost per request |
| 🔍 Tool Calls | Which tools the agent used and in what order |
| ❌ Errors | Failed API calls with full stack traces |

### Traced Functions
| Function | File | What it tracks |
|----------|------|----------------|
| `geocode-place` | `api_logic.py` | Geoapify geocoding latency |
| `get-nearby-places` | `api_logic.py` | Places API response time |
| `get-current-weather` | `api_logic.py` | OpenWeather API latency |
| `get-forecast-weather` | `api_logic.py` | Forecast API response time |
| `web-search` | `api_logic.py` | Tavily search latency |
| `plan-trip` | `api_logic.py` | Full trip planning chain |
| `get-places-for-agent` | `travel_tools_setup.py` | Agent places wrapper |
| `get-forecast-for-agent` | `travel_tools_setup.py` | Agent forecast wrapper |
| `plan-trip-for-agent` | `travel_tools_setup.py` | Agent trip wrapper |

### Setup LangSmith
1. Go to [smith.langchain.com](https://smith.langchain.com)
2. Create an account
3. Go to **Settings → API Keys → Create API Key**
4. Add to your `.env` file:
```env
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=your_key_here
LANGCHAIN_PROJECT=default
```

### Example Trace
```
AgentExecutor (68s, $0.0145)
├── ChatGoogleGemini        (8.21s, 556 tokens)
├── MultiDayTripPlanner     (6.95s)
│   ├── plan-trip-for-agent
│   │   └── plan-trip
│   │       ├── geocode-place        (1.73s)
│   │       ├── get-nearby-places    (4.01s)
│   │       └── get-forecast-weather (1.20s)
└── GetForecastWeather      (3.13s)
    └── get-forecast-for-agent
        └── geocode-place            (2.06s)
```

---

## 📁 Project Structure
```
travel_assistant/
├── app.py                  # FastAPI server & API endpoints
├── agent.py                # LangChain ReAct Agent + Gemini LLM + Memory
├── api_logic.py            # Core logic: Weather, Places, Trip Planning
├── travel_tools_setup.py   # LangChain Tool definitions
├── requirements.txt        # Python dependencies
├── dockerfile              # Docker configuration
├── .dockerignore           # Docker ignore file
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

Built with ❤️ using **LangChain + Google Gemini + FastAPI + Docker + LangSmith**