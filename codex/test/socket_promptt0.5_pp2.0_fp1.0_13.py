import socket
# Test socket.if_indextoname() on invalid input.

import unittest
from test import support

class If_indextonameTest(unittest.TestCase):

    def test_invalid_index(self):
        self.assertRaises(OverflowError, socket.if_indextoname, -1)
        self.assertRaises(OverflowError, socket.if_indextoname, 2 ** 32)
        self.assertRaises(OverflowError, socket.if_indextoname, 2 ** 64)
        self.assertRaises(OverflowError, socket.if_indextoname, 2 ** 128)
        self.assertRaises(OverflowError, socket.if_indextoname, 1.5)
        self.assertRaises(OverflowError, socket.if_indextoname, 1j)
        self.assertRaises(OverflowError, socket.if_indextoname, '1')
        self.assertRaises(OverflowError, socket.if_indextoname, None)
