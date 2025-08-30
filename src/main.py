import typer
from datetime import datetime
import subprocess
from pathlib import Path
import os

app = typer.Typer()

@app.command()
def hello(name: str):
    print(f"Hello {name}")

@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        print(f"Goodbye Ms. {name}. Have a good day.")
    else:
        print(f"Bye {name}!")

@app.command()
def add(entry: str = typer.Argument(None)):
    filename = datetime.now().strftime("%Y-%m-%d") + ".md"
    journal_dir = Path(os.path.expanduser("~/.journal"))
    journal_dir.mkdir(exist_ok=True)
    file_path = Path(journal_dir) / filename

    
    if entry:
        with open(file_path, "a") as f:
            timestamp = datetime.now().strftime("%H:%M")
            f.write(f"## {timestamp}\n{entry}\n\n")
        print(f"Entry '{entry}' added.")
    else:
        file_path.touch(exist_ok=True)
        subprocess.run(["vim", str(file_path)])

@app.command()
def list():
    journal_dir = Path(os.path.expanduser("~/.journal"))
    if not journal_dir.exists():
        print("No journal entries found.")
        return

    files = sorted(journal_dir.glob("*.md"), reverse=True)
    for file in files:
        print(file.name)

@app.command()
def view(date: str = typer.Argument(None)):
    journal_dir = Path(os.path.expanduser("~/.journal"))
    if date:
        filename = f"{date}.md"
    else:
        filename = datetime.now().strftime("%Y-%m-%d") + ".md"
    
    file_path = journal_dir / filename
    if file_path.exists():
        subprocess.run(["vim", str(file_path)])
    else:
        print(f"No entry found for {filename}")

@app.command()
def delete(date: str = typer.Argument(...)):
    journal_dir = Path(os.path.expanduser("~/.journal"))
    filename = f"{date}.md"
    file_path = journal_dir / filename
    if file_path.exists():
        file_path.unlink()
        print(f"Deleted entry for {date}.")
    else:
        print(f"No entry found for {date}.")


if __name__ == "__main__":
    app()