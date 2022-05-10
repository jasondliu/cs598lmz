import socket
# Test socket.if_indextoname()

import unittest
from test import support

class IfIndextonameTest(unittest.TestCase):

    def test_if_indextoname(self):
        # Test if_indextoname()
        self.assertRaises(TypeError, socket.if_indextoname, 1.0)
        self.assertRaises(TypeError, socket.if_indextoname, 1, 2)
        self.assertRaises(TypeError, socket.if_indextoname, None)
        self.assertRaises(ValueError, socket.if_indextoname, -1)
        self.assertRaises(ValueError, socket.if_indextoname, 0)
        self.assertRaises(OSError, socket.if_indextoname, 1)
        self.assertRaises(OSError, socket.if_indextoname, 65536)

def test_main():
    support.run_unittest(IfIndextonameTest)

if __name__ == "__main__":
    test_main
