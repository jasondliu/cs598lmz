import socket
# Test socket.if_indextoname()

import unittest
from test import support

class IfIndextonameTest(unittest.TestCase):

    def test_if_indextoname(self):
        ifname = socket.if_indextoname(1)
        self.assertTrue(ifname)
        self.assertTrue(isinstance(ifname, str))
        self.assertRaises(OSError, socket.if_indextoname, 0)
        self.assertRaises(OSError, socket.if_indextoname, -1)
        self.assertRaises(OSError, socket.if_indextoname, 65536)
        self.assertRaises(TypeError, socket.if_indextoname, "1")
        self.assertRaises(TypeError, socket.if_indextoname, None)
        self.assertRaises(TypeError, socket.if_indextoname)

def test_main():
    support.run_unittest(IfIndextonameTest)

