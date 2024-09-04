import json

# Load JSON from file
with open('data.json', 'r') as file:
    data = json.load(file)

# Write JSON to file
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)
