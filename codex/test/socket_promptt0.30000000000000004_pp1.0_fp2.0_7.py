import socket
# Test socket.if_indextoname()

import os, sys
import unittest
from test import support

class IfIndextonameTest(unittest.TestCase):

    def test_if_indextoname(self):
        # Make sure that if_indextoname() returns a string
        self.assertIsInstance(socket.if_indextoname(1), str)
        # Check that if_indextoname() raises an exception when passed an
        # invalid index
        self.assertRaises(OSError, socket.if_indextoname, -1)
        self.assertRaises(OSError, socket.if_indextoname, 0)
        self.assertRaises(OSError, socket.if_indextoname, 65536)

def test_main():
    support.run_unittest(IfIndextonameTest)

if __name__ == "__main__":
    test_main()
