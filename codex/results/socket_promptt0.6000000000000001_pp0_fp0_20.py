import socket
# Test socket.if_indextoname

import unittest

class TestIfIndextoname(unittest.TestCase):
    def test_if_indextoname(self):
        if_indextoname = socket.if_indextoname
        if_indextoname(1)
        self.assertRaises(OverflowError, if_indextoname, 2**32)
        self.assertRaises(OverflowError, if_indextoname, -1)
        self.assertRaises(OSError, if_indextoname, 0)
        self.assertRaises(OSError, if_indextoname, 2)

if __name__ == "__main__":
    unittest.main()
