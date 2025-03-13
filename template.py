# Importing the 'os' module, which provides functions to interact with the operating system 
# (e.g., creating directories, file manipulation).
import os  

# Importing 'Path' from the 'pathlib' module — a more modern and intuitive way to handle file paths.
# This makes path manipulation (joining paths, checking files, etc.) easier and cleaner than using os.path.
from pathlib import Path  

# Importing the 'logging' module to set up a logging system instead of using print statements.
# Logging is more powerful — it supports different levels like INFO, WARNING, ERROR, etc.
import logging  

# Configuring the logging system:
logging.basicConfig(
    level=logging.INFO,  # Sets the minimum log level to INFO — this excludes DEBUG logs but includes WARNING, ERROR, CRITICAL.
    format='[%(asctime)s] : %(message)s'  # Defines how the logs will look, showing a timestamp and the message.
)


list_of_files = [
    "source/__init__.py",     # Marks 'source' as a package, allowing imports from this folder.
    "source/utility.py",      # Contains utility functions to avoid code repetition
    "source/prompt.py",       # Likely handles user interactions or prompts
    ".env",                   # Stores environment variables (e.g., API keys, secrets, config values)
    "setup.py",      # Script to handle installation
    "app.py",        # Main core logic or launches the application
    "research/trials.ipynb"   # Jupyter Notebook for experiments, prototyping, or analysis.
]


# Looping through each file path listed in 'list_of_files'
for file_path in list_of_files:
    # Convert the file path string into a Path object (for cleaner path handling)
    filepath = Path(file_path)
    
    # Split the path into the directory part and the filename
    filedir, filename = os.path.split(filepath)


    # If the file path contains a directory (i.e., it's not an empty string)
    if filedir != "":
        # Create the directory if it doesn't exist (exist_ok=True prevents errors if it already exists)
        os.makedirs(filedir, exist_ok=True)
        # Log that the directory has been created (or already exists)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")


    # Check if the file doesn't exist OR it exists but is empty (size 0 bytes)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        # Open the file in write mode ("w"), which creates the file if it's missing
        with open(filepath, "w") as f:
            pass  # 'pass' keeps the file empty without writing anything
        # Log that an empty file was created
        logging.info(f"Creating an empty file {filepath}")

    # If the file already exists and is not empty, log that it's already there
    else:
        logging.info(f"{filename} already exists")
