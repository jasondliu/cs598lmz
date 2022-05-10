import socket
import sys
import time
import threading
import os

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))
        self.sock.listen(1)

    def handle_client(self, connection, address):
        try:
            while True:
                data = connection.recv(1024)
                if data:
                    print("Received: {}".format(data))
                    connection.sendall(data)
                else:
                    break
        finally:
            connection.close()

    def run(self):
        while True:
            connection, address = self.sock.accept()
            print("Connection from {}".format(address))
            client_handler = threading.Thread
