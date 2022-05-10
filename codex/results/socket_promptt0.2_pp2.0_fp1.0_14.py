import socket
# Test socket.if_indextoname()

import unittest
from test import support

class IfIndextonameTest(unittest.TestCase):

    def test_if_indextoname(self):
        # Test if_indextoname()
        self.assertTrue(socket.if_indextoname(1))
        self.assertRaises(ValueError, socket.if_indextoname, -1)
        self.assertRaises(ValueError, socket.if_indextoname, 0)
        self.assertRaises(OverflowError, socket.if_indextoname, 2**32)

def test_main():
    support.run_unittest(IfIndextonameTest)

if __name__ == "__main__":
    test_main()
