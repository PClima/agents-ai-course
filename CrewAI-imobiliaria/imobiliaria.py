import json
import os
from datetime import datetime, timedelta
from crewai import Agent, Task, Crew, Process
from crewai_tools import CSVSearchTool
from dotenv import load_dotenv, find_dotenv
from langchain.tools import Tool
from langchain_community.tools import DuckDuckGoSearchResults

input('')