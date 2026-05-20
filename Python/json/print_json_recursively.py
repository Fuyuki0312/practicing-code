import json

with open("test.json", "r") as f:
    json_data = json.load(f)

def print_json_content(json_content, indent=0):

    if isinstance(json_content, dict):
        for key, value in json_content.items():
            print(" "*indent + f"{key}:")
            print_json_content(value, indent=indent+4)
    elif isinstance(json_content, list):
        for index, item in enumerate(json_content):
            print(" "*indent + f"Item {index+1}:")
            print_json_content(item, indent=indent+4)
    else:
        print(" "*indent + str(json_content))

print_json_content(json_data)