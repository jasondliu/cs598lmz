import socket
# Test socket.if_indextoname

import socket
import unittest

class IfIndextonameTest(unittest.TestCase):

    def test_if_indextoname(self):
        self.assertRaises(OverflowError, socket.if_indextoname, 2**32)
        self.assertRaises(OverflowError, socket.if_indextoname, -1)
        self.assertRaises(OSError, socket.if_indextoname, 0)
        self.assertRaises(OSError, socket.if_indextoname, 1)
        self.assertRaises(OSError, socket.if_indextoname, 2)

if __name__ == "__main__":
    unittest.main()
