# Default target - show help when no argument is passed to make
.DEFAULT_GOAL := help

.PHONY: help install run dev test clean lint format sync

help: ## Show this help message
	@echo "Available commands:"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
	@echo ""
	@echo "Examples:"
	@echo "  make install    # Install dependencies"
	@echo "  make run        # Run the FastMCP server"
	@echo "  make dev        # Run in development mode"

install: ## Install project dependencies
	uv sync

install-test: ## Install test dependencies
	uv sync --extra test

run: ## Run the FastMCP server
	uv run python main.py

run-direct: ## Run FastMCP server directly with fastmcp command
	uv run fastmcp run main.py:mcp

run-http: ## Run FastMCP server with HTTP transport on port 8000
	uv run fastmcp run main.py:mcp --transport http --port 8000

dev: ## Run in development mode with auto-reload
	uv run python -m fastmcp.main main.py

test: ## Run pytest tests (starts server automatically)
	uv run pytest test_server.py -v

test-verbose: ## Run pytest tests with verbose output and print statements
	uv run pytest test_server.py -v -s

test-client: ## Test the FastMCP server with a client (requires server running)
	uv run python test_client.py

clean: ## Clean up temporary files
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	rm -rf .pytest_cache
	rm -rf build/
	rm -rf dist/

lint: ## Run linting checks
	uv run ruff check .

format: ## Format code
	uv run ruff format .

sync: ## Sync dependencies and lock file
	uv sync

version: ## Show FastMCP version
	uv run fastmcp version
