import socket
import sys
import time

from .base_client import BaseClient
from .base_client import User
from .base_client import Response

class TCPClient(BaseClient):

    def __init__(self, host, port, nick, *args):
        super(TCPClient, self).__init__(nick, *args)
        self.HOST = host
        self.PORT = port

    def connect(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.HOST, self.PORT))

    def read_data(self):
        try:
            data = self.sock.recv(1024)
            return data
        except:
            return None
            
    def send_data(self, data):
        self.sock.sendall(data)


if __name__ == '__main__':

    nick = sys.argv[1]
    client = TCPClient("localhost", 8888, nick)
    
    try:
        response =
