from dotenv import load_dotenv, find_dotenv
from crewai import Agent, Task, Crew, LLM
from langchain_groq import ChatGroq
import markdown
import pdfkit
import os

load_dotenv(find_dotenv())

llm = LLM(model="groq/gemma2-9b-it", api_key=os.environ['GROQ_API_KEY'], temperature=1)

sector = input("Wich sector do you want to analyze? (e.g. Artificial Intelligence, Health, etc.): ")
lang = input("Wich language do you want to use? (e.g. pt-BR, en): ")

#Agents
searcher = Agent(
    llm=llm,
    role="Market Researcher",
    goal="Collect and organize information about the market for a specific {sector}.",
    backstory="""
    You are experienced market researcher that analyzes market trends and collect relevant data 
    about {sector}. Your task is guarantee that all information is accurate and up to date.
    """,
    allow_dellegation=False,
    verbose=False
)
analyst = Agent(
    llm=llm,
    role="Tendencies Analyst",
    goal="Analyze the {sector} data and identify opportunities and patterns",
    backstory="""
    You are a market analyst that examines collected data to identify trends, opportunities and threats in the sector {sector}.
    """,
    allow_dellegation=False,
    verbose=False
)
writer = Agent(
    llm=llm,
    role="Report Writer",
    goal="Elaborate a consolidated report about the market {sector} analysis",
    backstory="""
    You are a professional report writer that transforms makert analysis data into a structured and clear report for decision making.
    """,
    allow_dellegation=False,
    verbose=False
)
translator = Agent(
    llm=llm,
    role="Translator",
    goal="Translate the report to {lang} language",
    backstory="""
    You are a professional translator that translates documents to {lang} language.
    """,
    allow_dellegation=False,
    verbose=False
)

#Tasks
data_collect = Task(
    description=(
        "1. Search and collect updated informations about the {sector} market. "
        "2. Identify the main players, tendencies and statistics about the {sector} market."
        "3. Organize the data clearly for the analyst."
    ),
    expected_output="A structured document containing the collected data about the {sector} market.",
    agent=searcher,
)
analysis_tendencies = Task(
    description=(
        "1. Analyze the searcher collected data about the {sector} market."
        "2. Identify patterns, emergent tendencies and opportunities in the sector {sector}."
        "3. Elaborate a detailed analysis destating the main points."
    ),
    expected_output="A report with insights and tendencies based on the collected data of sector {sector}.",
    agent=analyst,
)
report_write = Task(
    description=(
        "1. Use the tendencies analysis report to write a consolidated report about the {sector} market."
        "2. Guarantee that the report is clear, structured, comprehensive and with all relevant information."
        "3. Present the report in a professional format with final indications."
    ),
    expected_output="A analysis report about the {sector} market.",
    agent=writer,
)
translate = Task(
    description=(
        "1. Translate the report to {lang} language."
        "2. Guarantee that the translation is accurate and clear."
        "3. Present the report in a professional format."
    ),
    expected_output="A translated report in {lang} language in markdown format, ready to read and to presentation.",
    agent=translator,
)

# Crew
crew = Crew(
    agents=[searcher, analyst, writer, translator],
    tasks=[data_collect, analysis_tendencies, report_write, translate],
    verbose=True,
)
result = crew.kickoff(inputs={"sector": sector, "lang": lang})

with open("artigo.md", "w", encoding="utf-8") as file:
    file.write(str(result))

html = markdown.markdown(str(result))
with open("artigo.html", "w", encoding="utf-8") as file:
    file.write(str(html))