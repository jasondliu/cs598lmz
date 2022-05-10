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
        name = socket.if_indextoname(1)
        self.assertTrue(name)
        self.assertTrue(isinstance(name, str))
        self.assertRaises(ValueError, socket.if_indextoname, -1)
        self.assertRaises(ValueError, socket.if_indextoname, 0)
        self.assertRaises(OSError, socket.if_indextoname, sys.maxsize)

    def test_if_nameindex(self):
        # Test if_nameindex()
        nameindex = socket.if_nameindex()
        self.assertTrue(nameindex)
