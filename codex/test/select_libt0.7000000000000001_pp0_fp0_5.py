import selectors
import sys
import os

import socket

# Python3 only
#import socketserver


class Server:
    def __init__(self):
        self.sel = selectors.DefaultSelector()
        self.host = "localhost"
        self.port = 9000
        self.keep_running = True
        self.num_connections = 0
        self.num_connections_max = 10

    def run(self):
        lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        lsock.bind((self.host, self.port))
        lsock.listen()
        lsock.setblocking(False)
        self.sel.register(lsock, selectors.EVENT_READ, data=None)

