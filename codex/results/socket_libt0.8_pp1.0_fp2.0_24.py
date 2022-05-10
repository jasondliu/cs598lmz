import socket, termios, fcntl, sys, os
from select import select
from subprocess import Popen, PIPE
from threading import Thread

# /dev/ttyS0
TTY_DEV = sys.argv[1]
SERIAL_BAUD = 9600
SERIAL_TIMEOUT = None
SERIAL_PARITY = termios.PARITY_NONE
SERIAL_STOPBITS = termios.STOPBITS_ONE
SERIAL_DATABITS = termios.CS8

PROMPT_STR = 'pxshell> '
os.write(sys.stdout.fileno(), PROMPT_STR)

def serial_reader(fd, prompt_str):
    while True:
        # Read data from serial port
        data = fd.read(256)
        if data:
            os.write(sys.stdout.fileno(), data)
        else:
            # Timeout, write prompt
            os.write(sys.stdout.fileno(), prompt_str)

def serial_writer(fd):
    while True:

