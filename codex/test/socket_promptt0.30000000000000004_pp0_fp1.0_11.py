import socket
# Test socket.if_indextoname()

import unittest
from test import support

class IfIndextonameTest(unittest.TestCase):
    def test_if_indextoname(self):
        # Test if_indextoname()
        self.assertEqual(socket.if_indextoname(1), b'lo')

    def test_if_indextoname_invalid_index(self):
        # Test if_indextoname() with invalid index
        self.assertRaises(OSError, socket.if_indextoname, -1)
        self.assertRaises(OSError, socket.if_indextoname, 0)
        self.assertRaises(OSError, socket.if_indextoname, 65536)

    def test_if_indextoname_non_integer_index(self):
        # Test if_indextoname() with non-integer index
        self.assertRaises(TypeError, socket.if_indextoname, None)
