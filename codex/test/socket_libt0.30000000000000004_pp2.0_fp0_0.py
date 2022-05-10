import socket
import sys
import threading
import time
import random

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

def read_file():
    f = open('file.txt', 'r')
    file_content = f.read()
    f.close()
    return file_content

def write_file(data):
    f = open('file.txt', 'w')
    f.write(data)
    f.close()

