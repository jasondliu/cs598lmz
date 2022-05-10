import socket
import sys
import threading

class HTTP_SERVER:
    def __init__(self, port):
        self.port = port
        self.host = ''
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((self.host, self.port))
        self.server.listen(5)
        print('Server Starts - {}:{}'.format(self.host, self.port))

    def client_handler(self, client_socket, addr):
        request = client_socket.recv(1024).decode('utf-8')
        print(request)
