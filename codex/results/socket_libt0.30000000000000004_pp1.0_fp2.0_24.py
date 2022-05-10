import socket
import time
import sys
import os

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))
        self.socket.sendall(b'Hello, world')
        data = self.socket.recv(1024)
        print('Received', repr(data))
        self.socket.close()


if __name__ == '__main__':
    client = Client('127.0.0.1', 50000)
