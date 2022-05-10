import socket
# Test socket.if_indextoname()

import os
import sys
import unittest
from test import support

if not hasattr(socket, 'if_indextoname'):
    raise unittest.SkipTest("if_indextoname not defined")

class IfIndextonameTest(unittest.TestCase):

    def test_if_indextoname(self):
        # Test if_indextoname()
        self.assertRaises(OverflowError, socket.if_indextoname, 2**32)
        self.assertRaises(OverflowError, socket.if_indextoname, -1)
        self.assertRaises(TypeError, socket.if_indextoname, "1")
        self.assertRaises(TypeError, socket.if_indextoname, 1.0)
        self.assertRaises(TypeError, socket.if_indextoname, None)
        self.assertRaises(TypeError, socket.if_indextoname)
        self.assertRaises(TypeError, socket.if_indextoname,
