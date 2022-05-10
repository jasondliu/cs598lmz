import socket
# Test socket.if_indextoname()

import unittest
import os

from test import support
from test.support import TESTFN, find_unused_port, run_unittest

class IfIndextoNameTest(unittest.TestCase):
    def setUp(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.port = find_unused_port()
        self.sock.bind(('127.0.0.1', self.port))
        self.sock.listen(1)

    def tearDown(self):
        self.sock.close()
        del self.sock

    def testIfIndextoName(self):
        # Test socket.if_indextoname()
        self.assertRaises(ValueError, socket.if_indextoname, -1)
        self.assertRaises(ValueError, socket.if_indextoname, 0)
        self.assertRaises(ValueError, socket.if_indextoname, 1)
        self.
