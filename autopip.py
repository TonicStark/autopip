# Importing Libraries
from rich.console import Console
import subprocess
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
