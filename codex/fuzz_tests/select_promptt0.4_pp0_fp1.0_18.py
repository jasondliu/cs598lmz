import select
# Test select.select() with a timeout of zero.
import socket
import sys
import time
import unittest
from test import support
from test.support import find_unused_port

class SelectTestCase(unittest.TestCase):

    def setUp(self):
        self.serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.port = find_unused_port()
        self.serv.bind(('', self.port))
        self.serv.listen(5)

    def tearDown(self):
        self.serv.close()
        self.serv = None

    def client_connect(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('localhost', self.port))
        return client

    def test_select(self):
        # The test needs a non-blocking server socket, so set it to 0.5
        # seconds.  This should be enough time for any machine to accept
        # a client connection.
        self.serv.settimeout
