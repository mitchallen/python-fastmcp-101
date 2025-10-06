#!/usr/bin/env python3
"""
Test client to verify FastMCP server is working.
This script connects to the FastMCP server and tests the greet tool.
"""

import asyncio
import sys
from fastmcp import Client


async def test_server():
    """Test the FastMCP server by calling the greet tool."""
    client = Client("http://localhost:8000/mcp")
    
    try:
        async with client:
            print("Testing FastMCP server...")
            print("Connecting to: http://localhost:8000/mcp")
            
            # Test the greet tool
            result = await client.call_tool("greet", {"name": "Ford"})
            print(f"✅ Server response: {result}")
            
            # Test with a different name
            result2 = await client.call_tool("greet", {"name": "Arthur"})
            print(f"✅ Server response: {result2}")
            
            print("🎉 All tests passed! Server is working correctly.")
            return True
            
    except Exception as e:
        print(f"❌ Test failed: {e}")
        print("\nMake sure the FastMCP server is running:")
        print("  make run-http")
        return False


async def main():
    """Main function to run the test."""
    print("FastMCP Server Test Client")
    print("=" * 40)
    
    success = await test_server()
    
    if not success:
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())


