# Funtion to read and write the data. 
import json
def read(directory):
    try:
        with open(directory, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def write(directory,data):
    with open(directory, 'w') as file:
        json.dump(data,file,indent=4)