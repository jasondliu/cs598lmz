import socket
import time
import re
import hashlib

class HTTP():
    def __init__(self, host, port, http, timeout):
        self.host = host
        self.port = port
        self.http = http
        self.timeout = timeout
        self.socket = socket.socket()
        self.socket.settimeout(self.timeout)
        self.socket.connect((self.host, self.port))
        self.socket.send(self.http)

    def read(self):
        self.buffer = self.socket.recv(1024)
        return self.buffer

    def close(self):
        self.socket.close()

def get_host(uri):
    if re.match("(http|ftp|https)://", uri) is not None:
        uri = re.sub("(http|ftp|https)://", "", uri)
    uri = uri.split("/")
    return uri[0]

def get_port(uri):
    if re.match("(http|ftp|https)
