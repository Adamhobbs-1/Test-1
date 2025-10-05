from rich.console import Console
import sys
Console().rule("[bold]Hello from venv")
Console().print(f"Python: {sys.version.split()[0]}")
Console().print(f"Executable: {sys.executable}")

