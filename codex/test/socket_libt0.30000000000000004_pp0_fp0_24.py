import socket
import os
import sys
import time

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 8889)
print(f"connecting to {server_address}")
sock.connect(server_address)

