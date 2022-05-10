import mmap
import re
import os
import sys
import time

server_port = 50000

def main():

    # Create a TCP/IP socket
    print("Starting Python Server")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the port
    server_address = ('', server_port)
    print("Listening on port: " + str(server_port))
    sock.bind(server_address)

    # Listen for incoming connections
    sock.listen(1)

    while True:
        # Wait for a connection
        print("Waiting for a connection")
        connection, client_address = sock.accept()
