from fastapi import FastAPI, Request  # Importing FastAPI and Request from fastapi for building the API and handling requests
from tools import file_tools  # Importing file_tools from tools for file operations

app = FastAPI()  # Creating a FastAPI application

@app.post("/call_tool")  # Defining a POST endpoint for calling tools
async def call_tool(request: Request):  # The function is marked as async to handle asynchronous requests, like so it can perform opersionts on its own

    body = await request.json()  # Awaiting the JSON body of the request
    tool = body["tool"]  # Extracting the tool name from the request body
    args = body.get("args", {})  # Extracting arguments for the tool, defaulting to an empty dictionary if not provided

    if tool == "create_file":
        return {"result": file_tools.create_file(**args)}  # Calling create_file with arguments and returning the result
    elif tool == "read_file":
        return {"result": file_tools.read_file(**args)}  # Calling read_file with arguments and returning the result
    else:
        return {"error": "Tool not found"}  # Returning an error if the tool name does not match any of the expected tools


