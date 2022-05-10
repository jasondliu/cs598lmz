import socket
# Test socket.if_indextoname()

import sys, os
import unittest
from test import test_support

if not hasattr(socket, 'if_indextoname'):
    raise test_support.TestSkipped("if_indextoname not available")

# Test if_indextoname()

class IfIndextonameTest(unittest.TestCase):

    def test_if_indextoname(self):
        self.assertRaises(TypeError, socket.if_indextoname)
        self.assertRaises(TypeError, socket.if_indextoname, 1, 2, 3)
        self.assertRaises(OverflowError, socket.if_indextoname, 2**32)
        self.assertRaises(OverflowError, socket.if_indextoname, -1)
        self.assertRaises(ValueError, socket.if_indextoname, 0)
        self.assertRaises(ValueError, socket.if_indextoname, 1)
        self.assertRaises(OSError, socket.if_indext
