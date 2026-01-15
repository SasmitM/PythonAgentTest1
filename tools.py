from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_core.tools import StructuredTool
from datetime import datetime

def save_to_txt(data: str, filename: str = "research_output.txt") -> str:
    """Saves structured research data to a text file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f"--- Research Output ---\nTimestamp: {timestamp}\n\n{data}\n\n"

    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)
    
    return f"Data successfully saved to {filename}"

# Use the tools directly - they're already LangChain tools
search_tool = DuckDuckGoSearchRun()
wiki_tool = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=100))

# Create a structured tool for save
save_tool = StructuredTool.from_function(
    func=save_to_txt,
    name="save_text_to_file",
    description="Saves structured research data to a text file. Takes data as a string and optional filename."
)

