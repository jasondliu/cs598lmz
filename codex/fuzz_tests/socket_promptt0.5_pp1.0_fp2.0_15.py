import socket
# Test socket.if_indextoname() function
import sys
import unittest
from test import support

class IfIndexToNameTests(unittest.TestCase):
    def test_if_indextoname(self):
        if not hasattr(socket, "if_indextoname"):
            return
        # Issue #8121: if_indextoname() should return None for
        # invalid interfaces
        self.assertIsNone(socket.if_indextoname(-1))
        self.assertIsNone(socket.if_indextoname(sys.maxsize))


if __name__ == "__main__":
    unittest.main()
