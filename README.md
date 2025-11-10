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

To use this MCP server with Claude Code, you'll need to configure it in your Claude Code settings.

### 1. Configure the MCP Server

Add the server configuration to your Claude Code settings file:

```sh
code ~/.config/claude-code/settings.json
```

Add the following to the `mcpServers` section:

```json
{
  "mcpServers": {
    "fastmcp-101": {
      "command": "uv",
      "args": ["run", "main.py"],
      "cwd": "/Users/YOUR_USERNAME/projects/python/python-fastmcp-101"
    }
  }
}
```

**Note:** Replace `/Users/YOUR_USERNAME/projects/python/python-fastmcp-101` with the actual path to this project on your system.

### 2. Restart Claude Code

After saving the settings file, restart Claude Code to load the MCP server.

### 3. Test the Server

In Claude Code, you can test the server by asking:

```
Use the greet tool to say hello to Alice
```

Claude Code will automatically connect to your MCP server and use the `greet` tool defined in `main.py:12-16`.

### Troubleshooting

- **Server not appearing:** Check that the path in `cwd` is correct
- **Connection errors:** Ensure `uv` is installed (`brew install uv`)
- **Tool not found:** Verify the server started by checking Claude Code logs

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

