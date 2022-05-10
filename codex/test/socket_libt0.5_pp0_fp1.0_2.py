import socket
import sys
import threading
import time
import unittest

from . import test_utils


class TestSocket(unittest.TestCase):
    def setUp(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(('localhost', 0))
        self.server.listen(5)
        self.port = self.server.getsockname()[1]
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def tearDown(self):
        self.client.close()
        self.server.close()

    def test_connect_timeout(self):
        self.client.settimeout(0.1)
        self.assertRaises(socket.timeout, self.client.connect,
                          ('localhost', self.port))

    def test_sendall_timeout(self):
        self.client.connect(('localhost', self.port))
        self.client.settimeout(0.1)
