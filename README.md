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

