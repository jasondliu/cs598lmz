import socket
import select
import struct
import sys
import time

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = None
        self.connected = False
        self.buffer = ""
        self.read_buffer = ""
        self.write_buffer = ""

    def connect(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))
        self.connected = True

    def disconnect(self):
        self.socket.close()
        self.connected = False

    def send(self, data):
        self.write_buffer = data

    def recv(self):
        return self.read_buffer

    def process(self):
        if self.connected:
            readable, writable, exceptional = select.select([self.socket], [self.socket], [self.socket], 0)
            if readable:
                self.buffer += self.socket.recv(
