import select
import socket
import sys
import threading
import time
import traceback


class Server(object):
    """
    This class is responsible for listening for and accepting new connections
    from clients. When a new connection is made, it is handed off to the
    RequestHandler class to be managed.
    """
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = None
        self.request_handler = None

    def start(self):
        """
        This method starts the server and begins listening for new connections.
        """
        print("Starting server...")
        self.server_socket = socket.socket()
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        self.server_socket.setblocking(0)
        self.request_handler = RequestHandler()
        self.request_handler.start()
        print("Server ready")

        # Loop forever
        while True:
            try:
                # Wait until a client
