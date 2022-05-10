import signal
signal.signal(signal.SIGINT, signal_handler)
import time
import sys

names = {}

def restore_names(name_file_path):
    with open(name_file_path, 'r') as f:
        for line in f:
            name, num = line.split(': ')
            num = int(num)
            names[num] = name

def clear_names(name_file_path):
    with open(name_file_path, 'w') as f:
        pass

def update_name_list(name_file_path, num, name):
    if num not in names:
        names[num] = name
        with open(name_file_path, 'a') as f:
            f.write('{}: {}\n'.format(name, num))

def update_state(new_state):
    global state
    state = new_state
    print(state)

def identify_candidate(num):
    name = names[num]
