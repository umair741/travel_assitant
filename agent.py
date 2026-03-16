from langchain.agents import initialize_agent, AgentType
from langchain_google_genai import ChatGoogleGenerativeAI

from travel_tools_setup import tools
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage
import os
from dotenv import load_dotenv

load_dotenv()

def create_travel_agent():
    llm = ChatGoogleGenerativeAI(
        model="gemini-3-flash-preview",
        google_api_key=os.getenv("GOOGLE_API_KEY"),
        temperature=0.1,
        convert_system_message_to_human=True,
        system_instruction="Never use markdown formatting. No **, no ###, no *, no bullets. Use plain text and emojis only."
    )

    prompt = ChatPromptTemplate.from_messages([
        SystemMessage(content="""
You are a friendly and helpful Travel Assistant.

🎯 YOUR RESPONSIBILITIES:
- Help users plan multi-day trips
- Provide weather forecasts
- Suggest nearby places to visit
- Answer general travel questions

📋 TOOLS & WHEN TO USE THEM:

1. MultiDayTripPlanner - Plan day-wise trips
   - ALWAYS ask for number of days if not mentioned
   - Input: "CityName NumberOfDays" e.g. "Lahore 5"

2. GetForecastWeather - Weather forecast for a city
   - Input: city name e.g. "Karachi"

3. GetNearByPlaces - Find places in a city
   - Input: city name e.g. "Murree"

4. WebSearchTool - General travel info
   - Input: search query

📝 RESPONSE RULES:
- Plain text only
- NEVER use markdown like ###, **, *, --, or any special formatting
- Use emojis to make responses friendly
- Keep responses clean and readable
- Always end with a helpful follow-up question

⚠️ IMPORTANT:
- If user asks for trip plan without days, ask first!
- Never assume number of days
"""),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ])

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        handle_parsing_errors=True,  # ← added
        agent_kwargs={"prompt": prompt}
    )
    return agent

def main():
    agent = create_travel_agent()
    print("Travel Assistant Ready! (type 'exit' to quit)\n")

    while True:
        user_input = input("You: ")
        try:
            response = agent.invoke({"input": user_input})
            print("Assistant:", response["output"])
        except Exception as e:
            print("⚠️ Error:", e)