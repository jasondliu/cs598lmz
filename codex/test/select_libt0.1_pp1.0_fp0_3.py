import select
import socket
import sys
import threading
import time

import pytest

from . import util


class TestSocket(util.TestServer):
    def test_socket(self):
        self.assertEqual(self.loop.socket, socket.socket)

    def test_socket_close(self):
        sock = socket.socket()
        sock.close()
        self.loop.run_until_complete(self.loop.sock_connect(sock, self.addr))
        self.assertRaises(
            OSError, self.loop.run_until_complete,
            self.loop.sock_connect(sock, self.addr))

    def test_socket_close_twice(self):
        sock = socket.socket()
        sock.close()
        sock.close()

    def test_socket_connect_timeout(self):
        sock = socket.socket()
        sock.setblocking(False)
