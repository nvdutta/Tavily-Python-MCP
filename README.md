# Tavily Python MCP

Created as a demonstration of MCP servers. Anthropic's original sample server for Tavily MCP was written in typescript, so I made a python version to better suit one of my other projects.

# Claude Desktop Configuration

```
{
  "mcpServers": {
    "tavily-search": {
      "command": "uv",
      "args": [
        "--directory",
        "/your/project/path",
        "run",
        "tavily_server.py"
      ],
      "env": {
        "TAVILY_API_KEY": "your_api_key"
      }
    }
  }
}
```

Note: For windows machines, be sure to use \\ in place of / for the file path string.
