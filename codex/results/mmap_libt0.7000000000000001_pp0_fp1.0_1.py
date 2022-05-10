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
        try:
            print("Connection from " + client_address[0])

            # Receive the data in small chunks and retransmit it
            while True:
                data = connection.recv(16)
                print("Received: " + data)
                if data:
                    print("Sending client data back to client")
                    connection.sendall(data)
                else:
                   
