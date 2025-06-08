import google.generativeai as genai  
import requests                      # To call the MCP server
from dotenv import load_dotenv      # For loading API key from .env
from os import getenv               # For accessing environment variables



#need to load dotenv to get api key from .env
load_dotenv()

# Read the Gemini API key from environment
api_key = getenv("GEMINI_API_KEY")

#give error if api key is not found
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env")

#send in api key to genai
genai.configure(api_key=api_key)

#selected model
model = genai.GenerativeModel("gemini-1.5-flash")



# This function sends a tool call to the MCP server and returns the result
# For example: tool = "create_file", args = {"path": "main.py", "content": "print('Hi')"}
def call_mcp(tool: str, args: dict):
    response = requests.post("http://localhost:8000/call_tool", json={
        "tool": tool,
        "args": args
    })
    return response.json()



# This function is the core agent loop.
# It receives a user prompt, asks Gemini to respond with code, and uses a tool to save it.


def agent_prompt(prompt: str):

    #let user know what the prompt is
    print("Prompt to Gemini:", prompt)

    # Send the instruction to Gemini
    #my custom prompt
    response = model.generate_content(f"""
    You are an AI dev assistant. When a user gives a request,
    respond ONLY with the Python code inside triple backticks.
    Ignore everything else.
    User: {prompt}
    """)

    #get the response from the model
    reply = response.text

    #print the response
    print("\nAgent Thought:\n", reply)

    # Try to extract code from the response between triple backticks, becuase they use this convension for code
    if "```python" in reply:
        content = reply.split("```python")[1].split("```")[0].strip()
        file_name = "main.py"  # Default to main.py for now

        # Call MCP tool to create the file with the code
        result = call_mcp("create_file", {"path": file_name, "content": content})
        print("\n Tool Result:", result)
    else:
        print("No Python code found in response. Make sure the model responds correctly.")