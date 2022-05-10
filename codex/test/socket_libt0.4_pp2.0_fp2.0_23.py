import socket
import sys
import time
import os
import threading
import random

# HOST, PORT = "localhost", 9999
HOST, PORT = "10.0.0.1", 9999

USERNAME = "test"
PASSWORD = "test"

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server and send data
sock.connect((HOST, PORT))

# Send the username and password
sock.sendall(USERNAME + " " + PASSWORD)

# Receive data from the server and shut down
received = sock.recv(1024)

# Check if the user is authenticated
