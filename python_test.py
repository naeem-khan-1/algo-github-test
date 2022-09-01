import json
import random


def parse_data():
    with open('data.txt', 'r') as file:
        data = json.loads(file.read())
    parse_commands = [row.copy() for row in data if 'function' in row and row['function'] == 'parse']
    print(f"parse_commands: {parse_commands}")
    return parse_commands


def copy_data():
    with open('data.txt', 'r') as file:
        data = json.loads(file.read())
    copy_commands = [row.copy() for row in data if 'function' in row and row['function'] == 'copy']

    print(f"copy_commands: {copy_commands}")

    return copy_commands


def functional_data():
    # NOTE: Put the two lists together and say which list it came from as well as the item number for that list
    functional_commands = []
    counter = 0
    for row in functional_commands:
        counter += 1
        new_row = row.copy()
        new_row['_list'] = 'parse'
        new_row['_counter'] = counter
        functional_commands.append(new_row)
    counter = 0
    copy_commands = copy_data()
    for row in copy_commands:
        counter += 1
        new_row = row.copy()
        new_row['_list'] = 'copy'
        new_row['_counter'] = counter
        functional_commands.append(new_row)
    print(f"functional_commands: {functional_commands}")
    return functional_commands


def random_data():
    # NOTE: Get random sampling of data
    random_commands = []
    with open('data.txt', 'r') as file:
        data = json.loads(file.read())
        random_commands = random.sample(data, 2)
    print(f"random_commands: {random_commands}")
    return random_commands


def bad_data():
    with open('data.txt', 'r') as file:
        data = json.loads(file.read())

    bad_commands = []

    for row in data:
        if 'function' in row and row['function'] == 'bad value':
            bad_commands.append(row.copy())
        elif 'function' not in row and row['value'] == 'bad value':
            bad_commands.append(row.copy())

    print(f"bad_commands: {bad_commands}")

    return bad_commands
