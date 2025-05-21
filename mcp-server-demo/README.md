# MCP client server demo

## How to run client and server

First start server

```zsh
uv run python server.py
```

Now, lets run client

```zsh
uv run python client.py
```

Output from the client

```zsh
[05/21/25 21:57:30] INFO     Processing request of type CallToolRequest                                                                                                                    server.py:551
Result of add: meta=None content=[TextContent(type='text', text='8', annotations=None)] isError=False
                    INFO     Processing request of type ReadResourceRequest                                                                                                                server.py:551
Greeting: meta=None contents=[TextResourceContents(uri=AnyUrl('greeting://Alice'), mimeType='text/plain', text='Hello, Alice!')]
                    INFO     Processing request of type GetPromptRequest                                                                                                                   server.py:551
Code Review: meta=None description=None messages=[PromptMessage(role='user', content=TextContent(type='text', text="Please review the following code:\n\nprint('Hello, World!')", annotations=None))]
```
