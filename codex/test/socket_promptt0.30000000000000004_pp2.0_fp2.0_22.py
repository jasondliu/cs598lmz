import socket
# Test socket.if_indextoname()

import os
import sys
import unittest
import socket
from test import support

class IfIndextonameTest(unittest.TestCase):

    def test_if_indextoname(self):
        # Test if_indextoname()
        ifname = socket.if_indextoname(1)
        self.assertTrue(isinstance(ifname, str))
        self.assertTrue(ifname)
        self.assertRaises(ValueError, socket.if_indextoname, -1)
        self.assertRaises(ValueError, socket.if_indextoname, 0)
        self.assertRaises(OSError, socket.if_indextoname, 65536)

def test_main():
    support.run_unittest(IfIndextonameTest)

if __name__ == "__main__":
    test_main()
