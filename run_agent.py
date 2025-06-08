# run_agent.py
from agent_logic.agent import agent_prompt

if __name__ == "__main__":
    user_input = input("Enter your prompt: ")


    
    agent_prompt(user_input)