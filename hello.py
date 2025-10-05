from rich.console import Console
import sys, platform

c = Console()
c.rule("[bold]Hello from venv")
c.print(f"Python: {sys.version.split()[0]}")
c.print(f"Executable: {sys.executable}")
c.print(f"OS: {platform.system()} {platform.release()}")
c.rule("[bold]Goodbye from venv")
c.print("Goodbye from venv")