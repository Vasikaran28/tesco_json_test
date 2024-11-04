import json
import sys
import re

def validate_json(file_path):
    # Load and check JSON format
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        print("JSON file is valid format.")
    except json.JSONDecodeError as e:
        print(f"Invalid JSON format: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        sys.exit(1)

    # Check for required keys
    required_keys = {
        "name": str,
        "version": str,
        "dependencies": dict
    }
    for key, expected_type in required_keys.items():
        if key not in data:
            print(f"Error: Missing required key '{key}'")
            sys.exit(1)
        if not isinstance(data[key], expected_type):
            print(f"Error: Key '{key}' should be of type {expected_type.__name__}")
            sys.exit(1)

    # Optional: Validate version format (e.g., semantic versioning)
    version_pattern = r'^\d+\.\d+\.\d+$'  # Matches patterns like "1.0.0"
    if not re.match(version_pattern, data["version"]):
        print("Error: 'version' should follow semantic versioning (e.g., '1.0.0')")
        sys.exit(1)

    # Example additional checks (e.g., dependencies should have specific structure)
    if "dependencies" in data:
        if not all(isinstance(v, str) for v in data["dependencies"].values()):
            print("Error: All dependency versions should be strings")
            sys.exit(1)

    print("JSON file has valid structure and content.")

# Specify the JSON file to validate
file_path = 'tests/sample.json'  # Update this path if needed
validate_json(file_path)
