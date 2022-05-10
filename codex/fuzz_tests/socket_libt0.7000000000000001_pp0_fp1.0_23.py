import socket
import errno
import threading
import time
import os
import sys
import select

from util import *

## A simple class to represent a single proxy connection between a client and
## a server.
class ProxyConnection:
    def __init__(self, conn, addr):
        self.client_conn = conn
        self.client_addr = addr
        self.server_conn = None
        self.server_addr = None
        self.buffer = b''

    def _debug_print(self, *args, **kwargs):
        print('[{}:{}]'.format(self.client_addr[0], self.client_addr[1]), *args, **kwargs)

    def start(self):
        self._debug_print('Starting new connection.')

        ## YOUR CODE HERE
        # receive the HTTP request from the client
        data = self.client_conn.recv(4096)
        self.buffer += data
        if data:
            # parse the HTTP request and get the host
            try:
                request = HTTPRequest(self.buffer)
                self
