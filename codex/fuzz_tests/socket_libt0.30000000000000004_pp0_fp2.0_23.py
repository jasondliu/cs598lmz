import socket
import sys
import time
import threading
import os
import signal
import subprocess
import random

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

def signal_handler(signal, frame):
    print 'You pressed Ctrl+C!'
    sock.close()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def get_random_string(length):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))

def get_random_int(lower, upper):
    return random.randint(lower, upper)

def get_random_float
