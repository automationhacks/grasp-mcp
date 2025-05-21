import asyncio

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def demonstrate_capabilities():
    # Set up the server parameters
    server_params = StdioServerParameters(
        command="/Users/gauravsingh/.local/bin/uv",
        args=["run", "--with", "mcp", "python3", "server.py"],
        env=None
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # 1. Demonstrate the add tool
            print("\n=== Testing Add Tool ===")
            numbers = [(5, 3), (10, -2), (0, 0)]
            for a, b in numbers:
                result = await session.call_tool("add", {"a": a, "b": b})
                print(f"{a} + {b} = {result}")

            # 2. Demonstrate the greeting resource
            print("\n=== Testing Greeting Resource ===")
            names = ["Alice", "Bob", "Charlie"]
            for name in names:
                greeting = await session.read_resource(f"greeting://{name}")
                print(greeting)

            # 3. Demonstrate the code review prompt
            print("\n=== Testing Code Review Prompt ===")
            code_samples = [
                "print('Hello, World!')",
                "def factorial(n):\n    return 1 if n <= 1 else n * factorial(n-1)",
                "for i in range(10):\n    print(i)"
            ]
            
            for code in code_samples:
                review = await session.get_prompt("review_code", {"code": code})
                print(f"\nCode:\n{code}\nReview:\n{review}\n")


if __name__ == "__main__":
    asyncio.run(demonstrate_capabilities())
