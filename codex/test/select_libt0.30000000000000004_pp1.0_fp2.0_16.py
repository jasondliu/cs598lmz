import selectors
import socket
import types
import sys
import time
import threading
import random
import json
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

class Server:
    def __init__(self, port):
        self.sel = selectors.DefaultSelector()
        self.host = ''
        self.port = port
        self.lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.lsock.bind((self.host, self.port))
        self.lsock.listen()
        print('listening on', (self.host, self.port))
        self.lsock.setblocking(False)
        self.sel.register(self.lsock, selectors.EVENT_READ, data=None)
        self.clients = {}

    def accept_wrapper(self, sock):
        conn, addr = sock.accept()  # Should be ready to read
