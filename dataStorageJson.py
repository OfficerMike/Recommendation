import json

# Create some data to store
my_data = {'name': 'John Doe', 'age': 30, 'gender': 'male'}

# Open a file to store the data
with open('data.json', 'w') as f:
    # Serialize and store the data
    json.dump(my_data, f)

# Open the file and read the stored data back
with open('data.json', 'r') as f:
    # Deserialize and load the data
    loaded_data = json.load(f)

# Print the loaded data
print(loaded_data)