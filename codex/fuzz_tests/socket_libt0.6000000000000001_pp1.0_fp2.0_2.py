import socket
import sys

class Client():
    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))
        self.sock.setblocking(0)
        self.buffer_length = 1024
        self.buffer_store = ''
        self.cmd_store = []
        self.recv_data = ''

    def send_data(self, data):
        self.sock.send(data)
        if data[-1] != '\n':
            self.sock.send('\n')

    def recv_data(self):
        data = self.sock.recv(self.buffer_length)
        self.buffer_store += data
        while '\n' in self.buffer_store:
            message, self.buffer_store = self.buffer_store.split('\n', 1)
            self.cmd_store.append(message)

    def handle_data(self):
        if len
