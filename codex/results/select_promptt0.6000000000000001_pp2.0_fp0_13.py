import select
# Test select.select() for non-blocking sockets.
import socket
import unittest

from test import support
from test.support import find_unused_port
from test.support.script_helper import assert_python_ok

PORT = find_unused_port()


class NonBlockingTCPTests(unittest.TestCase):

    def setUp(self):
        self.serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serv.setblocking(False)
        self.serv.bind((HOST, PORT))
        self.serv.listen(5)

    def tearDown(self):
        self.serv.close()
        self.serv = None

    def test_recv(self):
        # Test receiving data on a non-blocking socket
        msg = b"xxx"
        self.cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.cli.setblocking(False)
        try:
            self.cli.connect((HOST, PORT))
       
