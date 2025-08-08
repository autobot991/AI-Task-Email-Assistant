
# tools/search_tool.py
import webbrowser
from agent import ask_llm  # Make sure this exists

def search_web(query):
    # Step 1: Open web browser
    search_url = f"https://duckduckgo.com/?q={query.replace(' ', '+')}"
    webbrowser.open(search_url)

    # Step 2: Summarize using LLM
    prompt = f"Search the web for: '{query}' and summarize the most relevant information."
    summary = ask_llm(prompt)

    return f"🔍 Opened search page in browser.\n\n🧠 Summary:\n{summary}"