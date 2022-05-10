import select
import socket
import sys
import time

#-------------------------------------------------------------------------------

class Server:
    """
    A simple TCP server.
    """

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        self.input_list = [self.server_socket]
        self.client_list = []

    def run(self):
        """
        Run the server.
        """
