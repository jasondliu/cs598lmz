import socket
# Test socket.if_indextoname()

import unittest
from test import support

class IfIndextonameTest(unittest.TestCase):

    def test_if_indextoname(self):
        ifname = socket.if_indextoname(1)
        self.assertTrue(ifname)
        self.assertTrue(isinstance(ifname, str))
        self.assertRaises(OverflowError, socket.if_indextoname, 2**32)
        self.assertRaises(OSError, socket.if_indextoname, -1)
        self.assertRaises(OSError, socket.if_indextoname, 0)

def test_main():
    support.run_unittest(IfIndextonameTest)

