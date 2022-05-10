import socket
# Test socket.if_indextoname()

import unittest
from test.support import run_unittest, socket_helper

class IfIndextonameTest(unittest.TestCase):

    def test_basic(self):
        self.assertRaises(OverflowError, socket.if_indextoname, -1)
        self.assertRaises(OverflowError, socket.if_indextoname, 2**32)
        self.assertRaises(OverflowError, socket.if_indextoname, 2**64)
        self.assertRaises(OverflowError, socket.if_indextoname, 2**100)
        self.assertRaises(OverflowError, socket.if_indextoname, -2**100)
        self.assertRaises(OverflowError, socket.if_indextoname, 2**1000)
        self.assertRaises(OverflowError, socket.if_indextoname, -2**1000)
        self.assertRaises(OverflowError, socket.if_indextoname, 2**10000)
        self.assert
