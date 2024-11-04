import json
import yaml
import os
import sys

def convert_json_to_yaml(json_path, yaml_path):
    try:
        # Load JSON data
        with open(json_path, 'r') as json_file:
            data = json.load(json_file)
        
        # Ensure the output directory exists
        os.makedirs(os.path.dirname(yaml_path), exist_ok=True)

        # Write YAML data
        with open(yaml_path, 'w') as yaml_file:
            yaml.dump(data, yaml_file, default_flow_style=False)
        
        print(f"Successfully converted {json_path} to {yaml_path}")
    except Exception as e:
        print(f"Error during conversion: {e}")
        sys.exit(1)

# Get file paths from environment variables
json_path = os.getenv('JSON_FILE_PATH', 'tests/sample.json')  # Default path if env variable is not set
yaml_path = os.getenv('YAML_FILE_PATH', 'tests/json_to_yml.yml')  # Default path if env variable is not set

convert_json_to_yaml(json_path, yaml_path)
