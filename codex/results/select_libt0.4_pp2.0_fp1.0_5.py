import selectors
import socket
import types
import sys
import time
import threading
import os
import time
import signal
import sys
import errno
import json
import logging

# HOST = '127.0.0.1'
# PORT = 65432

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.DEBUG)

class Server:
    def __init__(self, host, port, buffer_size=1024):
        self.host = host
        self.port = port
        self.buffer_size = buffer_size
        self.sel = selectors.DefaultSelector()
        self.messages = []
        self.clients = {}
        self.client_id = 0
        self.id_counter = 0

    def accept_wrapper(self, sock):
        conn, addr = sock.accept()  # Should be ready to read
        logging.debug('accepted connection from', addr)
        conn.setblocking(
