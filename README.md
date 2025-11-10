python-fastmcp-101
==

A quick intro to using [FastMCP](https://gofastmcp.com) to generate an MCP server.

## Usage 

```sh
make
```

```sh
make run-http
```

```sh
make test
```

* * *

## Testing with Claude Code on Mac

Claude Code supports MCP server configuration at different scopes. For this project, we'll use **local scope** so the server is only loaded when working in this directory.

### 1. Configure the MCP Server (Local Scope)

From this project directory, run:

```sh
claude mcp add --transport stdio fastmcp-101 --scope local -- uv run main.py
```

This command:
- Configures the server for **this project only** (not globally)
- Automatically uses the current directory as the working directory
- Stores the configuration in project-specific user settings

### 2. Restart Claude Code

After adding the server, restart Claude Code to load it.

### 3. Test the Server

In Claude Code, you can test the server by asking:

```
Use the greet tool to say hello to Alice
```

Claude Code will automatically connect to your MCP server and use the `greet` tool defined in `main.py:12-16`.

### Managing MCP Servers

```sh
# List all configured MCP servers
claude mcp list

# Get details for this server
claude mcp get fastmcp-101

# Remove this server
claude mcp remove fastmcp-101
```

### Configuration Scopes

- **Local scope** (recommended) - Project-specific, only loaded in this directory
- **Project scope** - Shared via `.mcp.json` file (committed to repo)
- **User scope** - Global across all projects

### Troubleshooting

- **Server not appearing:** Run `claude mcp list` to verify it's configured
- **Connection errors:** Ensure `uv` is installed (`brew install uv`)
- **Tool not found:** Check Claude Code logs for startup errors

* * *

## References

* [FastMCP](https://gofastmcp.com)
* [FastMCP Installation](https://gofastmcp.com/getting-started/installation)

### Hosting
* [Self-Hosted Remote MCP](https://gofastmcp.com/deployment/self-hosted)
* [FastMCP Cloud](https://fastmcp.cloud/)
* [FastMCP Cloud Guide](https://gofastmcp.com/deployment/fastmcp-cloud)

* * *

## Setup

### Install uv

```sh
brew install uv
```

### Init the project with uv

```sh
uv init
```

This will create the necessary project structure including:

* **pyproject.toml** - Project configuration file
* **README.md** (will be updated)
* **.python-version** - Python version specification
* Basic project structure

### Use uv to install FastMCP

```sh
uv add fastmcp
```

### Check the fastmcp version

#### Without a shell (recommended)

```sh
uv run fastmcp version
```

#### Within a shell 

```sh
uv shell
fastmcp version
exit
```

if you need to work in the virtual environment interactively:

#### First, sync dependencies (creates/updates the virtual environment)

```sh
uv sync
```

#### Then activate the virtual environment manually
#### On macOS/Linux, the virtual environment is typically at:

```sh
source .venv/bin/activate
```

#### Now you can run fastmcp directly

```sh
fastmcp version
```

#### When done, deactivate

```sh
deactivate
```

