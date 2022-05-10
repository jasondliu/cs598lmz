import socket
import sys
import time

from . import util

class Client(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def get(self, key):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            s.sendall(util.encode("get {}".format(key)))
            data = util.recv_all(s)
            return util.decode(data)

    def set(self, key, value):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            s.sendall(util.encode("set {} {}".format(key, value)))
            time.sleep(0.1)
            return True

