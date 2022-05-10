import socket
import sys
import threading
import pickle
from subprocess import Popen, PIPE

class Client:

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.sock.connect((self.ip, self.port))

    def send(self, msg):
        self.sock.send(msg)

    def recv(self):
        return self.sock.recv(1024)

    def close(self):
        self.sock.close()

