import select
import socket
import sys
import time
from pprint import pformat
import json

class TCP_Client(object):

    def __init__(self, ip, port = 5900):
        self.ip = ip
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.ip, self.port))
        self.buffsize = 4096
        self.connected_socket = None

    def __getattr__(self, name):
        if name in ['send', 'recv', 'fileno', 'connect', 'close']:
            return self.connected_socket.__getattribute__(name)
        return self.__getattribute__(name)

    def listen(self):
        self.sock.listen(1)
