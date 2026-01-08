# CrewAI Agent - Market Analyst

## General propose
The program has as general propose generate a market report about a specific sector, following the structure organized in three steps.
- Data collect
- Tendencies Analyst
- Report Writer

## Agents
### 1. Market Searcher
- ***Description***: This agent is responsible for collecting and organizing information about the market of a specific sector. It is dedicated to finding relevant data, identifying key players, and understanding sector trends. The main task of the Market Researcher is to ensure that all data is up-to-date and well-documented for further analysis.
- ***Objective***: Collect and organize detailed information about the sector to facilitate trend analysis and report preparation.

### 2. Tendencies Analyst
- ***Description***: The Tendencies Analyst examines the data collected by the Market Searcher and searches for patterns, opportunities, and threats in the sector. Responsible for conducting a deep analysis to identify emerging trends and the market dynamics that can affect the sector.
- ***Objective***: Examine sector data, identify trends, and generate insights to assist in decision-making.

### 3. Report Writer
- ***Description***: The Report Writer transforms data from the Tendencies Analyst agent into a structured and comprehensive report for decision-making. Creates final documentation with a clear vision of information and strategic recommendations based on market analysis.
- ***Objective***: Prepare a detailed report that synthesizes the findings and analysis of the sector, clearly presenting trends and actionable suggestions.

## Repositories
- crewai (orchestrator)
- crewai_tools (orchestrator)
- groq (AI interface)
- langchain_community (LLM framework)
- langchain_groq (LLM to AI)
- python-dotenv (env variables)
- pdfkit (file write)
- markdown (file write)