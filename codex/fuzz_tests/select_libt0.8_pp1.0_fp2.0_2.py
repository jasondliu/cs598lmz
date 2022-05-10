import select
import socket
import sys
import threading
import unittest
import zlib

from test import test_support
from test.test_support import verbose, TESTFN

if not hasattr(select, 'poll'):
    raise unittest.SkipTest("select.poll required for this test")

HOST = test_support.HOST

class TestSockets(unittest.TestCase):

    def setUp(self):
        self.serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.port = test_support.bind_port(self.serv)
        self.serv.listen(5)

    def tearDown(self):
        self.serv.close()
        self.serv = None

    def connect(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, self.port))
        return sock

    def test_recv(self):
        # Testing large receive over TCP
        msg = 'x' * (
