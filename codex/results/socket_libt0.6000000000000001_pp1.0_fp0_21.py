import socket
import sys
import time
from queue import Queue
from threading import Thread

from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Hash import SHA256
import base64

# AES encryption key
KEY = b'\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18'
# AES block size
BLOCK_SIZE = 16
# The padding character used with AES
PAD = '{'

# Set to True to print the server's responses
DEBUG = False

class ChatClient(object):
    def __init__(self, name, host, port):
        self.name = name
        self.connected = False
        self.host = host
        self.port = int(port)
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.setsockopt(socket
