import socket
import sys
import time
import threading
import random
import os

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

def send_file(file_name):
    f = open(file_name, 'rb')
    l = f.read(1024)
    while (l):
        sock.send(l)
        l = f.read(1024)
    f.close()

def receive_file(file_name):
    f = open(file_name, 'wb')
    l = sock.recv(1024)
    while (l):
        f.write(l)
        l = sock.recv(1024)
    f.close()

def send_message(message):
    sock.send(message)

