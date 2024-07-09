from tavily import TavilyClient
import os
from dotenv import load_dotenv

load_dotenv()

tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

class SearchAgent:
    def __init__(self):
        pass

    def search_tavily(self, query: str):
        results = tavily_client.search(query=query, topic="company overview", max_results=10)
        sources = results["results"]
        return sources

    def run(self, query: str):
        return self.search_tavily(query)

if __name__ == '__main__':
    search_agent = SearchAgent()
    query = "software companies"
    results = search_agent.run(query)
    print(results)