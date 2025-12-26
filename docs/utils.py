import os
import json
import logging
from typing import Any, Dict, List, Optional, Union

logger = logging.getLogger(__name__)

def read_json(filepath: str) -> Dict[str, Any]:
    """Read JSON file and return its content as a dictionary."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.error(f"Error reading JSON file {filepath}: {e}")
        raise

def write_json(data: Dict[str, Any], filepath: str, indent: int = 4) -> None:
    """Write dictionary data to a JSON file."""
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=indent)
    except (IOError, TypeError) as e:
        logger.error(f"Error writing JSON file {filepath}: {e}")
        raise

def create_directory(dirpath: str) -> None:
    """Create a directory if it doesn't exist."""
    try:
        os.makedirs(dirpath, exist_ok=True)
    except OSError as e:
        logger.error(f"Error creating directory {dirpath}: {e}")
        raise

def get_filepaths_from_dir(dirpath: str, extensions: Optional[List[str]] = None) -> List[str]:
    """Get all file paths from a directory, optionally filtered by extensions."""
    if not os.path.isdir(dirpath):
        raise ValueError(f"Directory {dirpath} does not exist.")

    filepaths = []
    for root, _, files in os.walk(dirpath):
        for file in files:
            if extensions is None or any(file.endswith(ext) for ext in extensions):
                filepaths.append(os.path.join(root, file))
    return filepaths

def setup_logging(log_file: Optional[str] = None, level: int = logging.INFO) -> None:
    """Configure logging to file and console."""
    handlers = [logging.StreamHandler()]
    if log_file:
        handlers.append(logging.FileHandler(log_file))

    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=handlers
    )