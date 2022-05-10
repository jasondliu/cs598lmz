import socket
# Test socket.if_indextoname() -- step #5

import os
import socket
import sys
import unittest

from test.support import run_unittest, TESTFN, find_unused_port


class SocketI2nTestCase(unittest.TestCase):
    def __init__(self, if_name):
        unittest.TestCase.__init__(self)
        self.TestIF = if_name

    def setUp(self):
        self.l_port = find_unused_port()
        self.l_addr = ("127.0.0.1", self.l_port)

    def tearDown(self):
        pass

    # Test if_indextoname() returns correct interface name
    def test_if_indextoname(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(self.l_addr)
        self.if_name = socket.if_indextoname(sock.getsockname()[-1])
        sock.close()
        #
