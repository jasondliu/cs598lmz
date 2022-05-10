import socket
import threading
import logging
import time
import sys
import os

#logging.basicConfig(level=logging.DEBUG, format='%(name)s: %(message)s',)

class Server:
    def __init__(self, host='', port=5000):
        self.clients = {}
        self.addresses = {}
        self.host = host
        self.port = port
        self.start_server()

    def start_server(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.host, self.port))
        self.sock.listen(5)
        self.sock.setblocking(False)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.quitting = False
        accept_thread = threading.Thread(target=self.accept_incoming_connections)
        accept_thread.start()
        accept
