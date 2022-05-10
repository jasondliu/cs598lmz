import select
# Test select.select on sockets, but use a moment when the sockets
# should be ready to avoid blocking.

import _socket
import select
import socket
import unittest
import time

# Test the constants
for name in (' POLLIN ', ' POLLPRI ', ' POLLOUT ', ' POLLERR ', ' POLLHUP ', ' POLLNVAL ', ):
    constant = getattr(select, name.strip())
    if not isinstance(constant, int):
        raise TypeError(
            '%s is not an integer: %r' % (name, constant))
    if constant != getattr(_socket, name.strip()):
        raise ValueError(
            '%s differs: select %r, _socket %r' % (name, constant, getattr(_socket, name.strip())))
del name, constant

class SelectTest(unittest.TestCase):
    def setUp(self):
        # Create two sockets
        self.serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
