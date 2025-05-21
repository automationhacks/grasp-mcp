import asyncio

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


server_params = StdioServerParameters(command="python3", args=["server.py"], env=None)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # Call the add tool
            result = await session.call_tool("add", {"a": 5, "b": 3})
            print(f"Result of add: {result}")

            # Call the get_greeting resource
            greeting = await session.read_resource("greeting://Alice")
            print(f"Greeting: {greeting}")

            # Call the review_code prompt
            code_review = await session.get_prompt("review_code",  {"code": "print('Hello, World!')"})
            print(f"Code Review: {code_review}")



if __name__ == "__main__":
    asyncio.run(run())
