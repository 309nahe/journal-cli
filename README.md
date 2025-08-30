# Journal CLI

A small command-line journaling tool in Python.  
Each day gets its own Markdown file inside `~/.journal`.

## Features
- `journal add "text"` → append a quick entry with a timestamp  
- `journal add` → open today’s file in vim for longer writing  
- `journal list` → list all existing journal files  
- `journal search "keyword"` → search for a keyword across all entries  
- `journal delete YYYY-MM-DD` → delete the journal file for a specific date  

Entries are saved as `~/.journal/YYYY-MM-DD.md`.

Example entry:

```markdown
## 23:41
This is a quick note
```

## Installation

Clone the repository and set up a virtual environment:

```bash
git clone https://github.com/yourname/journal-cli.git
cd journal-cli

python3 -m venv venv
source venv/bin/activate
pip install typer[all]
```

## Usage

Run with Python during development:

```bash
# Add a quick note
python3 main.py add "hello world"

# Open vim for today’s file
python3 main.py add

# List existing journal files
python3 main.py list

# Search across all journals
python3 main.py search "world"

# Delete a specific journal file (irreversible)
python3 main.py delete 2025-08-29
```

## Notes
- Files are stored in `~/.journal`. The directory is created automatically if missing.  
- The editor used for long entries is `vim`. Make sure it is installed and on your PATH.  
- Dates use the format `YYYY-MM-DD`.  
- This project uses [Typer](https://typer.tiangolo.com/) for the CLI.  