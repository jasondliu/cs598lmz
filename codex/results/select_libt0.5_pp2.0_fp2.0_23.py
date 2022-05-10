import select
import sys
import time
import os
import signal

def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

def read_input(fd):
    return os.read(fd, 1)

def output_char(fd, char):
    os.write(fd, char)

def output_string(fd, string):
    for char in string:
        output_char(fd, char)

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def print_help():
    output_string(1, "Enter a number between 0 and 9 to change the PWM duty cycle.\n")
    output_string(1, "Enter the letter 'h' for help.\n")
    output_string(1, "Enter the letter 'q' to quit.\n")
    output_string(1, "Enter the letter 's' to
