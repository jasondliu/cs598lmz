import socket
import sys
import time
import threading
import Queue
import random
import os

# Global variables
server_address = ('localhost', 10000)

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

def send_message(message):
    # Send data
    print >>sys.stderr, 'sending "%s"' % message
    sock.sendall(message)

def receive_message():
    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print >>sys.stderr, 'received "%s"' % data

def send_file(file_name):
    file_size = os.path
