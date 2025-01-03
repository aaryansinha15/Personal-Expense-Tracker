# Funtion to read and write the data. 
import json
# Read function is created for the to read the data. 
def read(directory):
    try:
        with open(directory, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# function to  write the data 

def write(directory,data):
    with open(directory, 'w') as file:
        json.dump(data,file,indent=4)