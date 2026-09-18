import httpx
import json
from fastmcp import FastMCP

# Create an HTTP client for your API
auth = httpx.BasicAuth("john.dunbar", "LY3^N?3f")
api_client = httpx.AsyncClient(
    base_url="https://fa-esfl-dev5-saasfademo1.ds-fa.oraclepdemos.com",
    auth=auth
)

# Load your OpenAPI spec 
filename = "/Users/pansaini/Documents/D/dev/launch_mcp/Launch_26b_OpenAPI.json"
with open(filename, 'r') as file:
    openapi_spec = json.load(file)

#print(openapi_spec)

#openapi_spec = httpx.get("https://api.example.com/openapi.json").json()

# Create the MCP server
mcp = FastMCP.from_openapi(
    openapi_spec=openapi_spec,
    client=api_client,
    name="Launch 26b API Server"
)

if __name__ == "__main__":
    mcp.run()

