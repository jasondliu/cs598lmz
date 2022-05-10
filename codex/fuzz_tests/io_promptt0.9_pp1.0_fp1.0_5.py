import io
# Test io.RawIOBase, we fake a socket connection
import urllib.request
import parsing
import requests


class client(object):
    def __init__(self, host, port):
        self.sc = socket.socket(type=socket.SOCK_STREAM)
        self.sc.connect((host, port))

    def send(self, msg):
        if not isinstance(msg, str):
            raise ValueError("message must be a string type")
        self.sc.send(msg.encode())

    def recv(self):
        return self.sc.recv(1024).decode()

    def close(self):
        self.sc.close()

    def __del__(self):
        self.sc.close()


class server(object):
    def __init__(self, host, port, listen=5):
        if isinstance(port, int) and int(port) in range(65535):
            self.port = port
        else:
            raise ValueError("Port number is invalid")
        self.ep = socket.socket(type=socket.SOCK
