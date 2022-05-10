import socket
# Test socket.if_indextoname()
# This test is not really complete, but it does test the function.

import unittest
import socket
from test import support

class IfIndextonameTest(unittest.TestCase):

    def test_if_indextoname(self):
        # This test is not really complete, but it does test the function.
        name = socket.if_indextoname(1)
        self.assertTrue(name)
        self.assertEqual(socket.if_indextoname(1), name)
        self.assertRaises(ValueError, socket.if_indextoname, 0)
        self.assertRaises(ValueError, socket.if_indextoname, -1)
        self.assertRaises(OSError, socket.if_indextoname, 1<<32)

if __name__ == "__main__":
    unittest.main()
