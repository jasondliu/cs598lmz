import mmap
import os
import signal
import socket


# Define our buffering size and packet header
BUFFER_SIZE = 1024
HEADER_LENGTH = 20
HOST = socket.gethostname()
PORT = 42069

# Specify the IP and PORT to use for the server
SERVER = (HOST, PORT)

# Create our socket and bind it to an IP/Port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(SERVER)

# We want our socket to listen for connections
s.listen()

# Define our method that will close the server on escape sequence
def closing():
    print("\nClosing the server")
    s.close()
    os._exit(0)

# Make the escape sequence close our server
signal.signal(signal.SIGINT, closing)

# This will be the dict of clients, their file name and their client socket
clients = {}

# This will be our dict of outgoing clients, their file name, dest IP and dest PORT
out
