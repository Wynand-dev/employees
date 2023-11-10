import random
import json

def generate_random_name():
    prefixes = ["Alpha", "Beta", "Gamma", "Delta", "Epsilon"]
    suffixes = ["Corp", "Industries", "Solutions", "Tech", "Labs"]

    random_name = random.choice(prefixes) + " " + random.choice(suffixes)
    return random_name

def generate_names_list(num_names):
    names_list = [generate_random_name() for _ in range(num_names)]
    return names_list

def save_to_json(names_list, filename):
    with open(filename, 'w') as json_file:
        json.dump(names_list, json_file, indent=2)

# Generate 10 random names and save them to a JSON file named 'random_names.json'
num_names = 10
names_list = generate_names_list(num_names)
save_to_json(names_list, 'random_names.json')
