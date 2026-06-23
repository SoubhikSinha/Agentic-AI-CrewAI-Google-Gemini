from dotenv import load_dotenv
load_dotenv()
import os

# Search Tool using Serper API
os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY')

from crewai_tools import SerperDevTool

# Initializing the tool for internet searching capabilities
tool = SerperDevTool()