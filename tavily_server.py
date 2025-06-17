import os
from typing import List
from mcp.server.fastmcp import FastMCP
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()

tavily_api_key = os.getenv("TAVILY_API_KEY")

# Initialize FastMCP server
mcp = FastMCP("Tavily"
              )

@mcp.tool()
def tavily_search(topic: str, max_results: int = 5) -> List[str]:
    """
    Perform a web search using Tavily for the given topic.
    
    Args:
        topic: The topic to search for
        max_results: Maximum number of results to retrieve (default: 5)
        
    Returns:
        Search results
    """
    # Use tavily for search
    client = TavilyClient(
        api_key=tavily_api_key
    )

    # Search for the most relevant articles matching the queried topic
    response = client.search(
        query = topic,
        max_results = max_results,
    )
    return response.get("results", [])

@mcp.tool()
def tavily_extract(urls: List[str]) -> List[str]:
    """
    Extract details from websites using Tavily.
    
    Args:
        topic: The topic to search for
        urls: The list of URLs to extract information from
        
    Returns:
        Extracted details from the URLs
    """
    # Use tavily for search
    client = TavilyClient(
        api_key="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"
    )

    # Search for the most relevant articles matching the queried topic
    response = client.extract(
        urls = urls
    )
    return response.get("results", [])

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(
        #transport='streamable-http'
        )