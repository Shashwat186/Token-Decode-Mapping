import json

# Replace 'your_file.json' with the path to your dictionary file
with open('combined_json.json', 'r') as file:
    dictionary = json.load(file)

# Count the number of keys
number_of_keys = len(dictionary)
print(f'Number of keys: {number_of_keys}')

