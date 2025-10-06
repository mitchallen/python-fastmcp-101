"""
Pytest tests for FastMCP server.
These tests start the server programmatically and test it with a client.
"""

import asyncio
import pytest
import subprocess
import time
import requests
from fastmcp import Client


class TestFastMCPServer:
    """Test class for FastMCP server functionality."""

    @pytest.fixture(scope="class")
    def server_process(self):
        """Start the FastMCP server process for testing."""
        # Start the server with HTTP transport
        process = subprocess.Popen([
            "uv", "run", "fastmcp", "run", "main.py:mcp", 
            "--transport", "http", "--port", "8000"
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Wait for server to start - look for startup message in stderr
        max_retries = 30
        for i in range(max_retries):
            try:
                # Check if server is running by looking for the startup message
                if process.poll() is None:  # Process is still running
                    # Try a simple connection test
                    import socket
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    result = sock.connect_ex(('localhost', 8000))
                    sock.close()
                    if result == 0:  # Port is open
                        break
            except Exception:
                pass
            time.sleep(0.5)
        else:
            # Get error output for debugging
            try:
                stdout, stderr = process.communicate(timeout=5)
                process.terminate()
                pytest.fail(f"Server failed to start within 15 seconds.\n"
                           f"STDOUT: {stdout.decode()}\n"
                           f"STDERR: {stderr.decode()}")
            except subprocess.TimeoutExpired:
                process.terminate()
                pytest.fail("Server process timed out during startup")
        
        yield process
        
        # Cleanup: terminate the server process
        process.terminate()
        process.wait()

    @pytest.mark.asyncio
    async def test_greet_tool(self, server_process):
        """Test the greet tool functionality."""
        client = Client("http://localhost:8000/mcp")
        
        async with client:
            # Test greeting with different names
            result1 = await client.call_tool("greet", {"name": "Ford"})
            assert result1.data == "Hello, Ford!"
            assert not result1.is_error
            
            result2 = await client.call_tool("greet", {"name": "Arthur"})
            assert result2.data == "Hello, Arthur!"
            assert not result2.is_error
            
            result3 = await client.call_tool("greet", {"name": "Zaphod"})
            assert result3.data == "Hello, Zaphod!"
            assert not result3.is_error

    @pytest.mark.asyncio
    async def test_greet_tool_edge_cases(self, server_process):
        """Test edge cases for the greet tool."""
        client = Client("http://localhost:8000/mcp")
        
        async with client:
            # Test with empty name
            result = await client.call_tool("greet", {"name": ""})
            assert result.data == "Hello, !"
            assert not result.is_error
            
            # Test with special characters
            result = await client.call_tool("greet", {"name": "Marvin 🤖"})
            assert result.data == "Hello, Marvin 🤖!"
            assert not result.is_error

    @pytest.mark.asyncio
    async def test_invalid_tool_call(self, server_process):
        """Test calling a non-existent tool."""
        client = Client("http://localhost:8000/mcp")
        
        async with client:
            # This should raise an exception for invalid tool
            with pytest.raises(Exception):
                await client.call_tool("nonexistent_tool", {"param": "value"})

    def test_server_health_check(self, server_process):
        """Test that the server is responding to HTTP requests."""
        # MCP endpoints typically return 406 for GET requests without proper headers
        # So we'll just check that we get a response (not a connection error)
        response = requests.get("http://localhost:8000/mcp", timeout=5)
        # MCP endpoints may return 406 for GET requests, which is expected
        assert response.status_code in [200, 406, 405]
