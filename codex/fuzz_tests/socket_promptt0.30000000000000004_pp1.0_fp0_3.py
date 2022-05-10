import socket
# Test socket.if_indextoname()

import unittest
from test import support
from test.support import socket_helper

class IfIndextonameTest(unittest.TestCase):

    def test_if_indextoname(self):
        # Test socket.if_indextoname()
        self.assertRaises(TypeError, socket.if_indextoname, None)
        self.assertRaises(OverflowError, socket.if_indextoname, 1<<32)
        self.assertRaises(OverflowError, socket.if_indextoname, -1)
        self.assertRaises(OSError, socket.if_indextoname, 0)
        self.assertRaises(OSError, socket.if_indextoname, 1<<31)

        # Test socket.if_indextoname() with valid index
        with socket_helper.transient_internet('www.python.org'):
            self.assertIsInstance(socket.if_indextoname(1), str)
            self.assertIsInstance(socket.if_indexton
