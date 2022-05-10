import select
import sys
import time

from . import util
from . import log
from . import config

class Socket(object):
    def __init__(self, sock, address, server):
        self.sock = sock
        self.address = address
        self.server = server
        self.recv_buffer = b''
        self.send_buffer = b''
        self.closed = False
        self.last_active = time.time()

    def fileno(self):
        return self.sock.fileno()

    def recv(self):
        try:
            data = self.sock.recv(config.BUFFER_SIZE)
        except socket.error as e:
            log.error('recv error: %s', e)
            self.close()
            return
        if not data:
            self.close()
            return
        self.recv_buffer += data
        self.last_active = time.time()

    def send(self):
        if not self.send_buffer:
            return
        try:
            sent = self
