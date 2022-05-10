import socket
# Test socket.if_indextoname()

import os
import sys
import unittest
from test import support

if not hasattr(socket, 'if_indextoname'):
    raise unittest.SkipTest("if_indextoname not defined")

class IfIndextoNameTest(unittest.TestCase):

    def test_if_indextoname(self):
        # Test if_indextoname()
        self.assertRaises(OverflowError, socket.if_indextoname, 2**32)
        self.assertRaises(OverflowError, socket.if_indextoname, -1)
        self.assertRaises(OSError, socket.if_indextoname, 0)
        self.assertRaises(OSError, socket.if_indextoname, 1)
        self.assertRaises(OSError, socket.if_indextoname, 2)
        self.assertRaises(OSError, socket.if_indextoname, 3)
