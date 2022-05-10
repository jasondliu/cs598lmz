import socket
import sys
import time

from common import *
from message import *
from error import *

class Client(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connected = False
        self.logged_in = False
        self.username = None
        self.last_message_id = 0
    def connect(self):
        self.socket.connect((self.host, self.port))
        self.connected = True
    def disconnect(self):
        self.socket.close()
        self.connected = False
    def send(self, message):
        if not self.connected:
            raise ClientError("Client not connected")
        message = json.dumps(message)
        message = message.encode()
        message_length = len(message)
        message_length_encoded = message_length.to_bytes(4, sys.byteorder)
