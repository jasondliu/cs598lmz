import socket
import sys
import time
import threading
import json
import random
import os

if len(sys.argv) != 2:
    print("Usage: python3 client.py [port]")
    exit()

PORT = int(sys.argv[1])

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', PORT)
print('connecting to %s port %s' % server_address)
sock.connect(server_address)

# Create a random number for the client
client_number = random.randint(1, 100)

# Create a thread to receive messages from the server
def receive_messages():
    while True:
        data = sock.recv(1024)
        if data:
            print("Received: " + data.decode())

# Start the thread
threading.Thread(target=receive_messages).start()

# Send the client number
