 
import json

def read_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def write_data(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)
