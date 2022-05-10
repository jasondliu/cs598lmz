import socket
import sys
import time
import threading
import os
import random
import string
import json

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

def randomword(length):
    return ''.join(random.choice(string.lowercase) for i in range(length))

def get_file_size(file_path):
    if os.path.isfile(file_path):
        file_info = os.stat(file_path)
        return file_info.st_size

def get_file_name(file_path):
    if os.path.isfile(file_path):
        return os.path.basename(file_path)

def get_file_ext(file
