import requests, re, datetime

README_FILE = "README.md"

def fetch_quote():
    try:
        r = requests.get("https://zenquotes.io/api/random").json()
        return f"_{r[0]['q']}_ — **{r[0]['a']}**"
    except:
        return "Error loading quote."

def fetch_stats():
    # You can replace this with GitHub API calls if needed
    return (
        "📁 Total Repos: 20\n"
        "⭐ Stars: 150\n"
        "🔃 Pull Requests: 45\n"
        "🐛 Issues Closed: 60"
    )

def replace_section(content, marker, new_text):
    pattern = f"<!-- START_SECTION:{marker} -->(.*?)<!-- END_SECTION:{marker} -->"
    replacement = f"<!-- START_SECTION:{marker} -->\n{new_text}\n<!-- END_SECTION:{marker} -->"
    return re.sub(pattern, replacement, content, flags=re.DOTALL)

with open(README_FILE, "r", encoding="utf-8") as f:
    readme = f.read()

updated_stats = fetch_stats()
updated_quote = fetch_quote()

readme = replace_section(readme, "stats", updated_stats)
readme = replace_section(readme, "quote", updated_quote)

with open(README_FILE, "w", encoding="utf-8") as f:
    f.write(readme)

print("README.md updated successfully!")
