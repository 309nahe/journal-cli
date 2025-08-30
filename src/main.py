import typer

app = typer.Typer()

@app.command()
def add(text: str = typer.Argument(None)):
    """
    Add a journal entry.
    If text is given, append it.
    If not, open vim.
    """
    if text:
        print(f"Appending: {text}")
    else:
        print("Opening vim...")

if __name__ == "__main__":
    app()
