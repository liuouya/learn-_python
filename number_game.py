#! /usr/bin/python3

import random

msgs = {
    'prologue':   'Guess what am I thinking? hint: 0 - 99',
    'too_low':    'Nah it\'s too low... try again!',
    'too_high':   'Nah it\'s too high... try again!',
    'nan':        'Is that even a number..? Try again!',
    'win':        'That\'s it! You won!',
    'new_record': 'Congrats this is a new record! You are smart!'
}

target = random.randint(0, 99)
record_path = 'record.txt'
records = False
record = False
attempts = 1

try:
    with open(record_path, 'r') as f:
        line = f.readline()
        record = False if line == '' else int(line)
except (FileNotFoundError, ValueError):
    record = False

print(msgs['prologue'])

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

if not record or attempts < record:
    print(msgs['new_record'])
    with open(record_path, 'w+') as f:
        f.write(str(attempts))
        f.close()
