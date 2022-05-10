import socket
import sys
import time
import threading
import os
import subprocess
import json
import re

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

def get_file_size(file_path):
    return os.stat(file_path).st_size

def get_file_name(file_path):
    return os.path.basename(file_path)

def get_file_extension(file_path):
    return os.path.splitext(file_path)[1]

def get_file_size_in_bytes(file_path):
    return os.path.getsize(file_path)

def get_file_size_in_mb(file_path):
    return os.path
