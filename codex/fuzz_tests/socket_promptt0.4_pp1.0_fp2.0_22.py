import socket
# Test socket.if_indextoname()

import unittest
from test import support

class IfIndexToNameTest(unittest.TestCase):
    def test_if_indextoname(self):
        # Test socket.if_indextoname()
        ifname = socket.if_indextoname(1)
        self.assertTrue(ifname)
        self.assertRaises(OverflowError, socket.if_indextoname, 2**32)
        self.assertRaises(OSError, socket.if_indextoname, -1)

def test_main():
    support.run_unittest(IfIndexToNameTest)

if __name__ == "__main__":
    test_main()
