import select
import socket
import sys
import threading
import time

import pytest

from . import utils, test_utils

# Skip these tests if we don't have the required modules
pytestmark = pytest.mark.skipif(
    not test_utils.HAS_PY3_SOCKET_MODULE,
    reason="requires the Python 3 socket module")


class TestSocket(utils.TestCase):

    def test_socket_create(self):
        # Create a socket object
        sock = socket.socket()
        self.addCleanup(sock.close)

        # Create a socket object using the fromfd() method
        if hasattr(socket, "fromfd"):
            fd = sock.fileno()
            sock2 = socket.fromfd(fd, sock.family, sock.type)
            self.addCleanup(sock2.close)

    def test_socket_close(self):
        # Closing a socket more than once should not raise an exception
        sock = socket.socket()
        sock.close()
        sock.close()

   
