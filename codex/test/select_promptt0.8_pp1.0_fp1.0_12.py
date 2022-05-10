import select
# Test select.select() for a single socket.
import select
import socket
import SocketServer
import sys
import time

def tohex(s):
    r = 0
    for c in s:
        r = (r << 8) | ord(c)
    return hex(r)

class FakeSocket(object):
    def __init__(self, src, dst, data):
        self.src = src
        self.dst = dst
        self.data = data
        self.connected = 1
        self.family = socket._getsockfamily(src)

    def getpeername(self):
        return self.dst

class SocketPairTest(unittest.TestCase):
    def setUp(self):
        self.sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock1.bind(("127.0.0.1", 0))
