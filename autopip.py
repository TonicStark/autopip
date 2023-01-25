# Importing Libraries
from rich.console import Console
import subprocess
import shutil
import sys
import os

# Global Console Object
console = Console()

# Getting the Project Path from Command Line
try:
    PRJ_PATH = sys.argv[1]
except IndexError:

    # Raising an Error Message
    console.print(
        "❌ [red]Error:[/red] you must use autopip [magenta]<.../to/project>[/magenta]!")

# Performing OS Operations using the given Path

# Check if the given Path exists:
if os.path.exists(PRJ_PATH):
    
    # Saving the Venv Path to delete
    venv_path = os.path.join(PRJ_PATH, "venv")

    # Deleting the Venv
    try:
        shutil.rmtree(venv_path)
    except FileNotFoundError:
        pass