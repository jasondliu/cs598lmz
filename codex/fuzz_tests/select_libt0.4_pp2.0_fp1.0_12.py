import selectors
import socket
import types
import sys
import os

# A class to handle the client connections
class Client:
    def __init__(self, server_addr, server_port, name):
        self.server_addr = server_addr
        self.server_port = server_port
        self.name = name
        self.sel = selectors.DefaultSelector()

    # A method to start the client
    def start(self):
        # Create a TCP socket
        lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set reuse address
        lsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # Bind the socket to the server address
        lsock.bind((self.server_addr, self.server_port))
        # Listen for incoming connections
        lsock.listen()
        # Print a message
        print('listening on', (self.server_addr, self.server_port))
        # Register the socket to be monitored for read events
       
