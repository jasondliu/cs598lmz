import socket
import sys
import json
import traceback

class Client(object):

    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))
        print("Connected to " + host + ":" + str(port))
        self.id = None

