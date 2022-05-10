import socket
import time
import sys
import os

# Set up the host and port
host = 'localhost'
port = 8080

# Create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
s.connect((host, port))

# Receive the welcome message
welcome = s.recv(1024)
