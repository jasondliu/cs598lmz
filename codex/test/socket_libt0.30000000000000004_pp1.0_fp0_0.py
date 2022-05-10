import socket
import sys
import os
import time

class Client:
    def __init__(self, host, port, name):
        self.host = host
        self.port = port
        self.name = name
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))
        self.sock.send(self.name.encode())
        self.sock.setblocking(0)
        self.sock.settimeout(1)
        self.sock.send(b'\n')
        self.sock.send(b'\n')
        self.sock.send(b'\n')
        self.sock.send(b'\n')
        self.sock.send(b'\n')
        self.sock.send(b'\n')
        self.sock.send(b'\n')
        self.sock.send(b'\n')
