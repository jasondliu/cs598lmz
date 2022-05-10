import socket
# Test socket.if_indextoname()

import os, sys
import unittest
from test import support

class IfIndextonameTest(unittest.TestCase):

    def test_if_indextoname(self):
        # Test socket.if_indextoname()
        # Get all interfaces on this host
        for i in range(256):
            try:
                name = socket.if_indextoname(i)
            except OSError:
                continue
            self.assertIsInstance(name, str)
            self.assertTrue(name)
        self.assertRaises(OSError, socket.if_indextoname, 256)
        self.assertRaises(OSError, socket.if_indextoname, -1)
        self.assertRaises(TypeError, socket.if_indextoname)

def test_main():
    support.run_unittest(IfIndextonameTest)

if __name__ == "__main__":
    test_main()
