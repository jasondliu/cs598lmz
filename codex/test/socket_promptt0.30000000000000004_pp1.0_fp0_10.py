import socket
# Test socket.if_indextoname()

import unittest
from test import support

class IfIndextonameTestCase(unittest.TestCase):

    def test_if_indextoname(self):
        # Test if_indextoname()
        self.assertRaises(ValueError, socket.if_indextoname, -1)
        self.assertRaises(ValueError, socket.if_indextoname, 256)
        self.assertRaises(OSError, socket.if_indextoname, 256)
        self.assertRaises(OSError, socket.if_indextoname, -1)
        self.assertRaises(TypeError, socket.if_indextoname)
        self.assertRaises(TypeError, socket.if_indextoname, None)
        self.assertRaises(TypeError, socket.if_indextoname, 'a')
        self.assertRaises(TypeError, socket.if_indextoname, 1, 2)
