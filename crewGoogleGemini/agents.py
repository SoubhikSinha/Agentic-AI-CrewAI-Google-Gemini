from tools import tool
from crewai import Agent

from dotenv import load_dotenv
import os

load_dotenv()

# CrewAI uses LiteLLM under the hood, so pass the model name as a string
# using the "gemini/<model>" format. Set the API key in the environment.
os.environ["GEMINI_API_KEY"] = os.getenv("GOOGLE_API_KEY", "")

llm = "gemini/gemini-3.5-flash"

# Creating the agents
'''
Creating a senior researcher agent with memory and verbose mode
'''
news_researcher=Agent(
    role="Senior Researcher",
    goal='Unccover ground breaking technologies in {topic}',
    verbose=True, # If this is set to True, the agent will print its thoughts and actions to the console
    memory=True, # If this is set to True, the agent will remember the previous conversation and use it to inform its responses.
    backstory=(
        "Driven by curiosity, you're at the forefront of"
        "innovation, eager to explore and share knowledge that could change"
        "the world."

    ),
    tools=[tool], # Serper is used for internet searching capabilities
    llm=llm,
    allow_delegation=True # If this is set to True, the agent will be able to delegate tasks to other agents.

)

'''
Creating a write agent with custom tools responsible in writing news blog
'''
news_writer = Agent(
  role='Writer',
  goal='Narrate compelling tech stories about {topic}',
  verbose=True,
  memory=True,
  backstory=(
    "With a flair for simplifying complex topics, you craft"
    "engaging narratives that captivate and educate, bringing new"
    "discoveries to light in an accessible manner."
  ),
  tools=[tool], # Serper is used for internet searching capabilities
  llm=llm,
  allow_delegation=False
)