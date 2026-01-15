# Python AI Agent From Scratch

A research assistant AI agent built with LangChain that can search the web, query Wikipedia, and save research results in a structured format. This project demonstrates how to build an AI agent from scratch using modern Python libraries.

## Features

- **Web Search**: Uses DuckDuckGo to search the internet for information
- **Wikipedia Integration**: Queries Wikipedia for detailed information on topics
- **Structured Output**: Returns research results in a structured JSON format with topic, summary, sources, and tools used
- **File Saving**: Saves research results to a text file for future reference
- **Tool Calling**: Demonstrates how AI agents can use multiple tools to complete research tasks

## Project Structure

```
PythonAIAgentFromScratch/
├── main.py              # Main agent logic and orchestration
├── tools.py             # Tool definitions (search, Wikipedia, save)
├── requirements.txt     # Python dependencies
├── sample.env          # Environment variable template
└── README.md           # This file
```

## Prerequisites

- Python 3.8 or higher (tested with Python 3.13)
- OpenAI API key
- Virtual environment (recommended)

## Installation

1. **Clone or navigate to the project directory:**
   ```bash
   cd PythonAIAgentFromScratch
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   - Copy `sample.env` to `.env`
   - Add your OpenAI API key:
     ```
     OPENAI_API_KEY="your-api-key-here"
     ```

## Usage

1. **Activate your virtual environment** (if not already active):
   ```bash
   source .venv/bin/activate
   ```

2. **Run the agent:**
   ```bash
   python main.py
   ```

3. **Enter your research query** when prompted:
   ```
   What can i help you research? 
   ```

4. **The agent will:**
   - Search the web and Wikipedia for relevant information
   - Compile a structured response with topic, summary, and sources
   - Display the results in a formatted output
   - Optionally save results to `research_output.txt`

## Example Output

The agent returns structured data in the following format:

```python
ResearchResponse(
    topic="Your research topic",
    summary="Comprehensive summary of the research findings...",
    sources=["source1", "source2", ...],
    tools_used=["search", "wiki_tool", ...]
)
```

## How It Works

1. **Agent Creation**: Uses LangChain's `create_agent` function with GPT-4o model
2. **Tool Integration**: Provides the agent with three tools:
   - `search_tool`: DuckDuckGo web search
   - `wiki_tool`: Wikipedia queries
   - `save_tool`: File saving functionality
3. **Structured Output**: Uses Pydantic to enforce a structured response format
4. **Execution**: Agent autonomously decides which tools to use based on the query

## Technologies Used

- **LangChain**: Framework for building LLM applications
- **OpenAI GPT-4o**: Large language model for agent reasoning
- **LangChain Community**: Community tools (Wikipedia, DuckDuckGo)
- **Pydantic**: Data validation and structured output
- **Python-dotenv**: Environment variable management

## Tools

### Search Tool
- **Source**: DuckDuckGo Search
- **Purpose**: Search the web for current information
- **Implementation**: `DuckDuckGoSearchRun` from LangChain Community

### Wikipedia Tool
- **Source**: Wikipedia API
- **Purpose**: Get detailed, encyclopedic information
- **Implementation**: `WikipediaQueryRun` with configurable result limits

### Save Tool
- **Purpose**: Save research results to a text file
- **Output**: Appends to `research_output.txt` with timestamps

## Configuration

You can customize the agent by modifying:

- **Model**: Change `model="openai:gpt-4o"` in `main.py` to use a different model
- **Tools**: Add or remove tools in `tools.py`
- **Output Format**: Modify the `ResearchResponse` class in `main.py`
- **Wikipedia Results**: Adjust `top_k_results` and `doc_content_chars_max` in `tools.py`

## Troubleshooting

### Import Errors
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Verify you're using the correct virtual environment
- Make sure `ddgs` package is installed (required by `duckduckgo-search`)

### API Key Issues
- Verify your `.env` file exists and contains `OPENAI_API_KEY`
- Ensure the API key is valid and has credits

### Python Version Compatibility
- This project is tested with Python 3.13
- Some older Python versions may require adjustments

## Future Enhancements

- Add more tools (PDF parsing, database queries, etc.)
- Implement conversation history
- Add support for multiple LLM providers
- Create a web interface
- Add result caching

## License

This project is open source and available for educational purposes.

## Contributing

Feel free to fork this project and submit pull requests with improvements!
