import socket
# Test socket.if_indextoname()

import sys
import os
import unittest
from test import support

if not hasattr(socket, 'if_indextoname'):
    raise unittest.SkipTest("if_indextoname not available on this platform")

class InterfaceTest(unittest.TestCase):

    def test_basic(self):
        # Test basic functionality.
        name = socket.if_indextoname(1)
        self.assertTrue(name)
        self.assertEqual(socket.if_indextoname(1), name)
        self.assertEqual(socket.if_nametoindex(name), 1)

    def test_invalid_args(self):
        # Test invalid arguments.
        self.assertRaises(OverflowError, socket.if_indextoname, 10**9)
        self.assertRaises(OverflowError, socket.if_nametoindex, 'a' * 256)
        self.assertRaises(TypeError, socket.if_indextoname)
