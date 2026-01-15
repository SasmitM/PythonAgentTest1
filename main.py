from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_agent
from tools import search_tool, wiki_tool, save_tool

load_dotenv()

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]
    

parser = PydanticOutputParser(pydantic_object=ResearchResponse)

system_prompt = f"""You are a research assistant that will help generate a research paper.
Answer the user query and use necessary tools. 
Wrap the output in this format and provide no other text:
{parser.get_format_instructions()}
"""

tools = [search_tool, wiki_tool, save_tool]
agent = create_agent(
    model="openai:gpt-4o",
    tools=tools,
    system_prompt=system_prompt
)

query = input("What can i help you research? ")
raw_response = agent.invoke(
    {"messages": [{"role": "user", "content": query}]}
)

try:
    # Extract the output from the agent response
    # create_agent returns a state dict with messages
    if isinstance(raw_response, dict) and "messages" in raw_response:
        # Get the last AI message content
        messages = raw_response["messages"]
        output_text = None
        for msg in reversed(messages):
            if hasattr(msg, 'content') and msg.content:
                output_text = msg.content
                break
            elif isinstance(msg, dict) and 'content' in msg:
                output_text = msg['content']
                break
        
        if not output_text:
            output_text = str(messages[-1])
    elif isinstance(raw_response, dict) and "output" in raw_response:
        output_text = raw_response["output"]
    else:
        output_text = str(raw_response)
    
    structured_response = parser.parse(output_text)
    print(structured_response)
except Exception as e:
    print("Error parsing response", e, "Raw Response - ", raw_response)