import select
import socket
import sys
import time

from OpenSSL import SSL

#-------------------------------------------------------------------------------

class _Connection(object):
    """
    A connection to a client.
    """
    def __init__(self, sock, addr):
        self.sock = sock
        self.addr = addr
        self.buffer = ""
        self.closed = False
        self.last_active = time.time()
        self.ssl = None
        self.ssl_handshaked = False

    def fileno(self):
        return self.sock.fileno()

    def close(self):
        if self.sock:
            self.sock.close()
            self.sock = None
        self.closed = True

    def clear(self):
        self.close()
        self.buffer = ""

    def read(self, length=4096):
        """
        Read from the connection, returning any data that's available.
        """
        try:
            if self.ssl:
                data = self.ssl.read(length)
            else:
                data
