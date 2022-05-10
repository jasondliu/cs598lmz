import select
# Test select.select with various timeout values
import socket
import time
import unittest
from test import support
from test.support import find_unused_port
from test.support.script_helper import assert_python_ok

# Create a socket pair
sock1, sock2 = socket.socketpair()

# Create a socket pair using AF_UNIX stream sockets
sock3, sock4 = socket.socketpair(socket.AF_UNIX, socket.SOCK_STREAM)

# Test the constants
for name in ('POLLIN', 'POLLPRI', 'POLLOUT', 'POLLERR', 'POLLHUP', 'POLLNVAL'):
    assert hasattr(select, name), name
    assert isinstance(getattr(select, name), int), name

# Test the poll() function
pollster = select.poll()
pollster.register(sock1)
pollster.register(sock2, select.POLLIN | select.POLLPRI)
pollster.register(sock3, select.POLLOUT)
pollster.register(sock
