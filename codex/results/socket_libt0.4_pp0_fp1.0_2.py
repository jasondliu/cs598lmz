import socket
from . import abstract_transport

class Transport(abstract_transport.AbstractTransport):
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def send_message(self, message):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            s.sendall(message)
