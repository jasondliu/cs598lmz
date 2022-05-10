import socket
# Test socket.if_indextoname()

import unittest
from test import support

class IfIndextonameTest(unittest.TestCase):

    def test_if_indextoname(self):
        # Check that if_indextoname() returns a string
        self.assertTrue(isinstance(socket.if_indextoname(1), str))

    def test_if_indextoname_invalid_index(self):
        # Check that if_indextoname() raises an exception for an invalid index
        self.assertRaises(OSError, socket.if_indextoname, -1)
        self.assertRaises(OSError, socket.if_indextoname, 0)
        self.assertRaises(OSError, socket.if_indextoname, 65536)

    def test_if_indextoname_invalid_type(self):
        # Check that if_indextoname() raises an exception for an invalid type
        self.assertRaises(TypeError, socket.if_indextoname, None)
