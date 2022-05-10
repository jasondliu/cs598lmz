import socket
import sys
import time
import threading
import os
import subprocess
import signal

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

def handle_client(client_connection):
    while True:
        data = client_connection.recv(1024)
        if data:
            print >>sys.stderr, 'received "%s"' % data
            client_connection.sendall(data)
        else:
            print >>sys.stderr, 'no more data from', client_address
            break

def handle_client_with_timeout(client_connection):
    while True:
        data = client_connection.recv(1024)
        if data:
            print >>sys.stderr
