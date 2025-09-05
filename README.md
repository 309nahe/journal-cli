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

Clone the repository:

```bash
git clone https://github.com/yourname/journal-cli.git
cd journal-cli
Install system-wide with pip (recommended):
pip install --user -e .
```

## Usage

```bash
# Add a quick note
journal add "hello world"

# Open vim for today’s file
journal add

# List existing journal files
journal list

# Search across all journals
journal search "world"

# Delete a specific journal file (irreversible)
journal delete 2025-08-29

```

## Notes
- Files are stored in `~/.journal`. The directory is created automatically if missing.  
- The editor used for long entries is `vim`. Make sure it is installed and on your PATH.  
- Dates use the format `YYYY-MM-DD`.  
- This project uses [Typer](https://typer.tiangolo.com/) for the CLI.  