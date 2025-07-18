from mcp.server.fastmcp import FastMCP

mcp = FastMCP("My First MCP Server")

@mcp.tool()
def get_weather(location:str)->str:
    """
    Get the current weather for a given location.
    """
    # This is a placeholder implementation.
    # In a real application, you would call a weather API here.
    return f"The current weather in {location} is sunny with a temperature of 25°C."

@mcp.resource("weather://{location}")
def weather_resource(location:str) -> str:
    """
    A resource that provides weather information.
    """
    return f"Weather resource in {location} is sunny with a temperature of 25°C."

@mcp.prompt()
def weather_report(location:str) -> str:
    """
    Create a weather report prompt
    """
    return f"You are a weather reporter. Get the weather report for {location}."

if __name__ == "__main__":
    mcp.run()
