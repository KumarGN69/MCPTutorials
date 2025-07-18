import asyncio, os
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


server_params = StdioServerParameters(
    command="python",
    args=["server.py"],
    env=None
)

async  def run():
    """Run the client session with the server parameters."""
    async with stdio_client(server_params) as (read, write) :
        async with ClientSession(read, write) as session:
            await session.initialize()

            resources = await session.list_resource_templates()
            prompts = await session.list_prompts()
            tools = await session.list_tools()
            print(resources)
            print(prompts)
            print(tools)

            # for resource in resources:
            #     print(f"Resource:{resource}")
            # for prompt in prompts:
            #     print(f"Prompt:{prompt}")
            # for tool in tools:
            #     print(f"Tool:{tool}")

def main():
    asyncio.run(run())

if __name__ == "__main__":
    main()