import socket
# Test socket.if_indextoname()

import os
import sys
import unittest
import socket

from test import support

if not hasattr(socket, 'if_indextoname'):
    raise unittest.SkipTest("socket.if_indextoname not defined")

class IfIndextonameTest(unittest.TestCase):

    def test_if_indextoname(self):
        # Issue #7995: if_indextoname() should not crash if passed an invalid
        # index.
        self.assertRaises(OSError, socket.if_indextoname, -1)
        self.assertRaises(OSError, socket.if_indextoname, 0x7fffffff)

def test_main():
    support.run_unittest(IfIndextonameTest)

if __name__ == "__main__":
    test_main()
