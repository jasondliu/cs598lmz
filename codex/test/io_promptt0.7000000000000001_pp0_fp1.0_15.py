import io
# Test io.RawIOBase to create raw socket connection to host.
import socket
import time
import random

# Default to a random hostname.
HOST = "localhost"
PORT = random.randint(1024, 65535)

class Socket(io.RawIOBase):
    """A Raw I/O implementation based on a socket object."""

    def __init__(self):
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._sock.connect((HOST, PORT))
        self._sock.setblocking(0)
        self._sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

    def readinto(self, b):
        try:
            return self._sock.recv_into(b)
        except socket.error as e:
            if e.errno == errno.EAGAIN:
                return None
            raise

    def write(self, b):
        return self._sock.send(b)

