import socket
# Test socket.if_indextoname()

from test.support import run_unittest, socket_helper
import unittest
import os

class IfIndextonameTest(unittest.TestCase):

    def test_if_indextoname(self):
        if not hasattr(socket, 'if_indextoname'):
            self.skipTest('socket.if_indextoname() required')
        self.assertRaises(OverflowError, socket.if_indextoname, 10**9)
        self.assertRaises(OverflowError, socket.if_indextoname, -1)
        self.assertRaises(TypeError, socket.if_indextoname)
        self.assertRaises(TypeError, socket.if_indextoname, 'a')
        self.assertRaises(TypeError, socket.if_indextoname, 1, 2)
        self.assertRaises(OSError, socket.if_indextoname, 1)
        self.assertRaises(OSError, socket.if_indextoname, -1)

