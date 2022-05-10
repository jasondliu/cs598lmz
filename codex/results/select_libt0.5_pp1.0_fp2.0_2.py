import select
import socket
import sys
import threading

from . import common


class Server(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)

        self.socket_list = [self.server_socket]
        self.clients = {}
        self.addresses = {}

    def run(self):
        print('Server is listening on port {}'.format(self.port))
        while True:
            read_sockets, write_sockets, exception_sockets = select.select(self.socket_list, [], self.socket_list)

            for sock in read_sockets:
                if sock == self.server_socket
