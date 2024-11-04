import json
import yaml
import os
import sys

def convert_json_to_yaml(json_path, yaml_path):
    try:
        # Load JSON data
        with open(json_path, 'r') as json_file:
            data = json.load(json_file)
        
        print(f"Loaded JSON data from {json_path}: {data}")

        # Ensure the output directory exists
        output_dir = os.path.dirname(yaml_path)
        os.makedirs(output_dir, exist_ok=True)
        print(f"Output directory checked/created: {output_dir}")

        # Write YAML data
        with open(yaml_path, 'w') as yaml_file:
            yaml.dump(data, yaml_file, default_flow_style=False)
        
        print(f"Successfully converted {json_path} to {yaml_path}")
    except Exception as e:
        print(f"Error during conversion: {e}")
        sys.exit(1)

# Specify the file paths
json_path = os.path.join('tests', 'sample.json')  # This will point to tests/sample.json
yaml_path = os.path.join('tests', 'json_to_yml_test.yml')  # This will point to tests/json_to_yml.yml

convert_json_to_yaml(json_path, yaml_path)
