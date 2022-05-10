import socket
import sys
import json

class Client():
    def __init__(self, server_address, port, filename):
        self.server_address = server_address
        self.port = port
        self.filename = filename
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

