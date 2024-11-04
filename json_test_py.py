# validate_json.py
import json
import sys

def validate_json(file_path):
    try:
        with open(file_path, 'r') as file:
            json.load(file)
        print("JSON file is valid.")
    except json.JSONDecodeError as e:
        print(f"Invalid JSON: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        sys.exit(1)

# Specify the JSON file to validate
file_path = 'tests/sample.json'  # Update with the correct path
validate_json(file_path)
