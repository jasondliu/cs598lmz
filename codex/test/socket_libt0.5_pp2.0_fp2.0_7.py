import socket
import sys
import time
import threading
import os

if __name__ == '__main__':

    HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
    PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the port
    server_address = (HOST, PORT)
    print(sys.stderr, 'starting up on %s port %s' % server_address)
    sock.bind(server_address)

    # Listen for incoming connections
    sock.listen(1)

    def client_thread(connection):
        while True:
            data = connection.recv(1024)
            print(data)
            connection.sendall(b'pong')
            if not data:
                break

