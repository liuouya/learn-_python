#! /usr/bin/python3

import random
import pickle

default_lower_bound = 0
default_upper_bound = 99

msgs = {
    'prologue':   'Give me a range to think about :)',
    'prompt':     'What am I thinking?',
    'lower_bound':'Lower bound (default ' + str(default_lower_bound) + '):',
    'upper_bound':'Upper bound (default ' + str(default_upper_bound) + '):',
    'too_low':    'Nah it\'s too low... try again!',
    'too_high':   'Nah it\'s too high... try again!',
    'nan':        'Is that even a number..? Try again!',
    'win':        'That\'s it! You won!',
    'new_record': 'Congrats this is a new record! You are smart!'
}

# start
print(msgs['prologue'])

# get range
lower_bound = input(msgs['lower_bound'])
upper_bound = input(msgs['upper_bound'])
target_range = (int(default_lower_bound if lower_bound == '' else lower_bound),
                int(default_upper_bound if upper_bound == '' else upper_bound))
target = random.randint(target_range[0], target_range[1])

# load records
record_path = 'number_game.record'
records = {}
record = False
attempts = 1

try:
    records = pickle.load(open(record_path, 'rb+'))
    record = records[target_range] if target_range in records else False
except (FileNotFoundError, EOFError):
    record = False

# main game loop
print(msgs['prompt'])
while True:
    try:
        guess = int(input())
        if guess == target:
            print(msgs['win'])
            break
        print(msgs['too_low'] if guess < target else msgs['too_high'])
    except (ValueError):
        print(msgs['nan'])
    attempts += 1

# store new record
if not record or attempts < record:
    print(msgs['new_record'])
    records[target_range] = attempts
    pickle.dump(records, open(record_path, 'wb+'))
