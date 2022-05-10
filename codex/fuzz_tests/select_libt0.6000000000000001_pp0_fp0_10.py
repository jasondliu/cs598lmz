import selectors
import sys
import time


class SocketServer:
    def __init__(self, address):
        self.address = address
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.selector = selectors.DefaultSelector()
        self.clients = {}

    def start_server(self):
        self.server_socket.bind(self.address)
        self.server_socket.listen()
        self.server_socket.setblocking(False)
        self.selector.register(self.server_socket, selectors.EVENT_READ, self.accept_connection)

    def accept_connection(self, server_socket, mask):
        client_socket, addr = server_socket.accept()
        print('Accepted connection from ', addr)
        client_socket.setblocking(False)
        self.selector.register(client_socket, selectors.EVENT_READ, self.read_message)
        self.clients[client_socket] = {'data': b'', 'addr
