# Importing Libraries
from rich.console import Console
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

# Saving the Venv Path to delete
venv_path = os.path.join(PRJ_PATH, "venv")

# Check if the given Path exists:
if os.path.exists(PRJ_PATH):

    # Deleting the Venv
    try:
        shutil.rmtree(venv_path)
    except FileNotFoundError:
        pass

    # Creating a New Venv
    os.chdir(PRJ_PATH)
    os.system("python -m venv venv")

    # Creating a list of unfiltered packages
    unfiltered_packages = []

    # Opening the file and appending each line to the list
    with open("requirements.txt", "r") as f:
        unfiltered_packages = f.readlines()
    
    # Clearing the list
    packages_list = [package.split("=")[0] for package in unfiltered_packages]

    # Installing the Packages in the New Environment
    PIP = "venv\Scripts\pip.exe"
    for pkg in packages_list:
        os.system(f"{PIP} install {pkg}")