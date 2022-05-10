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

def recv_cmd_output(client):
    while True:
        try:
            buf = client.recv()
            if len(buf) > 0:
                print buf
        except:
            client.close()
            sys.exit(0)

def recv_cmd_input(client):
    while True:
        try:
            buf = raw_input()
            if
