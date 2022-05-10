import socket
# Test socket.if_indextoname()

import os
import sys
import unittest
from test import support

if not hasattr(socket, 'if_indextoname'):
    raise unittest.SkipTest("if_indextoname not defined")

class IfIndextoNameTest(unittest.TestCase):

    def test_if_indextoname(self):
        # Test if_indextoname()
        ifname = socket.if_indextoname(1)
        self.assertTrue(ifname)
        self.assertTrue(isinstance(ifname, str))
        self.assertRaises(ValueError, socket.if_indextoname, -1)
        self.assertRaises(ValueError, socket.if_indextoname, 0)
        self.assertRaises(OSError, socket.if_indextoname, 0x7fffffff)

def test_main():
    support.run_unittest(IfIndextoNameTest)

if __name__ == "__main__":
    test_main()
