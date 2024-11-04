import json
import yaml
import sys

def convert_json_to_yaml(json_path, yaml_path):
    try:
        # Load JSON data
        with open(json_path, 'r') as json_file:
            data = json.load(json_file)
        
        # Write YAML data
        with open(yaml_path, 'w') as yaml_file:
            yaml.dump(data, yaml_file, default_flow_style=False)
        
        print(f"Successfully converted {json_path} to {yaml_path}")
    except Exception as e:
        print(f"Error during conversion: {e}")
        sys.exit(1)

# Specify the file paths
json_path = 'tests/sample.json'  # Replace with your JSON file path
yaml_path = 'tests/json_to_yml.yml'  # Replace with your desired YAML file path

convert_json_to_yaml(json_path, yaml_path)
