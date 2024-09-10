import json
import os

data_list = []
new_json = {}

# Collect JSON files and sort them based on their numeric key
for file in os.listdir():
    if file.endswith(".json") and file[:-5].isdigit():  # Ensure the key is numeric
        data_list.append(file)

# Sort the files numerically based on the key (before the .json extension)
data_list.sort(key=lambda x: int(x.split(".")[0]))

# Load and combine JSON files in the sorted order
for file in data_list:
    try:
        with open(file, "r") as fp:
            key = file.split(".")[0]
            new_json[key] = json.load(fp)
    except (json.JSONDecodeError, IOError) as e:
        print(f"Error reading {file}: {e}")

# Write the combined JSON data to a new file
try:
    with open('new_json.json', "w") as fp:
        json.dump(new_json, fp, indent=4)
except IOError as e:
    print(f"Error writing new_json.json: {e}")
