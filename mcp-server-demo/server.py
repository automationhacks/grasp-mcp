import asyncio

from mcp.server.fastmcp import FastMCP


mcp = FastMCP("Demo")


@mcp.tool()
def add(a: int, b: int) -> int:
    return a + b


@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    return f"Hello, {name}!"


@mcp.prompt()
def review_code(code : str) -> str:
    return f"Please review the following code:\n\n{code}"


if __name__ == "__main__":
    asyncio.run(mcp.run())