import socket
# Test socket.if_indextoname()

import socket
import unittest
from test import support

class IfIndextonameTest(unittest.TestCase):

    def test_if_indextoname(self):
        # Test if_indextoname()
        self.assertRaises(ValueError, socket.if_indextoname, -1)
        self.assertRaises(ValueError, socket.if_indextoname, 0)
        self.assertRaises(ValueError, socket.if_indextoname, 65536)
        self.assertRaises(ValueError, socket.if_indextoname, 2**32)
        self.assertRaises(ValueError, socket.if_indextoname, 2**64)
        self.assertRaises(ValueError, socket.if_indextoname, -2**64)

        # Test if_indextoname() with a valid index
        self.assertIsInstance(socket.if_indextoname(1), str)

    def test_if_indextoname_with_invalid_index(self):
