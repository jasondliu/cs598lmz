import socket
# Test socket.if_indextoname()

import socket
import unittest
from test import support
from test.support import os_helper

class TestIfIndextoname(unittest.TestCase):
    def test_ifindextoname(self):
        if not hasattr(socket, 'if_indextoname'):
            self.skipTest('socket.if_indextoname not available')
        self.assertIsInstance(socket.if_indextoname(1), str)
        self.assertEqual(socket.if_indextoname(1), 'lo')
        self.assertRaises(OSError, socket.if_indextoname, 0)
        self.assertRaises(OverflowError, socket.if_indextoname, 2**32)
        self.assertRaises(TypeError, socket.if_indextoname, '1')


if __name__ == "__main__":
    unittest.main()
