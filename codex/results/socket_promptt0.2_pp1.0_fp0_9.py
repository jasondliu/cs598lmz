import socket
# Test socket.if_indextoname()

import os
import sys
import unittest
import socket
from test import support

class IfIndextonameTest(unittest.TestCase):

    def test_if_indextoname(self):
        ifname = socket.if_indextoname(1)
        self.assertTrue(isinstance(ifname, str))
        self.assertTrue(len(ifname) > 0)

    def test_if_indextoname_invalid_index(self):
        self.assertRaises(OSError, socket.if_indextoname, 0)
        self.assertRaises(OSError, socket.if_indextoname, -1)
        self.assertRaises(OSError, socket.if_indextoname, -2)
        self.assertRaises(OSError, socket.if_indextoname, -3)
        self.assertRaises(OSError, socket.if_indextoname, -4)
        self.assertRaises(OSError, socket.if_indextoname, -5)

