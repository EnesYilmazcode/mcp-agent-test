from fastapi import FastAPI, Request  # handling requests
from tools import file_tools  # needed for file operations

app = FastAPI()  # Creating a FastAPI application

@app.post("/call_tool")  # POST endpoint for calling tools
async def call_tool(request: Request):  # The function is marked as async to handle asynchronous requests, like so it can perform opersionts on its own


    body = await request.json()  # Awaiting the JSON body of the request

    tool = body["tool"]  # getting the tool name from the request body

    args = body.get("args", {})  # getting arguments for the tool, return empty dictionary if not provided


    if tool == "create_file":
        return {"result": file_tools.create_file(**args)}  # create tool
    elif tool == "read_file":
        return {"result": file_tools.read_file(**args)}  # read tool
    else:
        return {"error": "Tool not found"}


