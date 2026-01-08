# CrewAI Agent - Realtor

## General Purpose
The program simulates a complete real estate consultancy, where the client receives a detailed analysis of available properties, market trends, relevant news, and financing options. The workflow is organized and structured into various tasks and agents, who collaborate to provide the client with the best options based on data and market analysis.

The final process is managed by CrewAI, which is a set of agents that collaborate to perform tasks related to property search and recommendation, price trend analysis, and financing. The system executes this process through a series of interactions between the agents and generates the desired result.

## Agents
### 1. Realtor
- ***Description***: This is an agent responsible for gathering client preferences (like property models, price, location, etc.). A specialist in the real estate market, it performs searches using the CSVSearchTool.
- ***Objective***: Find the best property options based on client preferences.
- ***Tool***: CSVSearchTool (to search properties in a CSV file)

### 2. Real Estate Market Analyst
- ***Description***: This is an agent responsible for analyzing price trends in various cities, helping to estimate market appreciation or depreciation. It uses data series to gather information about price trends.
- ***Objective***: Analyze price history and generate insights from it.
- ***Tool***: TendenciePricePropertyTool (to analyze price trends in a specific town)

### 3. Real Estate News Analyst
- ***Description***: This agent searches for recent news about the real estate market, analyzing external factors such as economic changes or events that may impact property prices.
- ***Objective***: Obtain relevant information about the real estate market through news and external trends.
- ***Tool***: DuckDuckGoSearchResults (to search for news about real estate and the economy)

### 4. Financial Consultant
- ***Description***: This agent helps analyze the client's income and suggests viable financing options for property purchases, considering interest rates and terms offered by financial institutions.
- ***Objective***: Provide financing options based on the client's financial conditions.
- ***Tool***: N/A

### 5. Report Writer
- ***Description***: This agent generates persuasive and well-structured reports about the properties recommended to clients. It considers analyses, trends, and financing options to create a final report.
- ***Objective***: Create a detailed report about the chosen property, including market analysis and financial options.
- ***Tool***: N/A