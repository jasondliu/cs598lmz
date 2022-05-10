import socket
import os
import sys
import hashlib
import time
import pickle

class Client:
    def __init__(self, socket):
        # Waiting for input
        self.addr = (socket.gethostbyname(socket.gethostname()), 5555)
        print(self.addr)
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.connect(self.addr)
        self.socket = socket
        self.message = ""
        self.delay = 1
        self.count = 1
        self.s.sendto(pickle.dumps(" "), self.addr)
        self.files = {}
        self.files = pickle.loads(self.s.recv(2048))
        print(self.files)
        self.fileName = None
        self.fileIndex = 0

# Check for available files
    def checkAvailable(self, filename):
        print(self.files)
        if filename in self.files.keys():
            return True
        return False

