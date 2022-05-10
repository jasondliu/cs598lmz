import socket
import time
import os

class Client:
    def __init__(self, host, port, timeout=None):
        try:
            self.sock = socket.create_connection((host, port), timeout)
        except socket.error as err:
            raise ClientError("Client error: {}".format(err))

    def put(self, key, value, timestamp=None):
        timestamp = timestamp or int(time.time())
        try:
            self.sock.sendall("put {} {} {}\n".format(key, value, timestamp).encode("utf8"))
            self.get_response()
        except socket.error as err:
            raise ClientError("Client error: {}".format(err))

    def get(self, key):
        try:
            self.sock.sendall("get {}\n".format(key).encode("utf8"))
            return self.get_response()
        except socket.error as err:
            raise ClientError("Client error: {}".format(err))

    def get_response(self):
        data = b""
