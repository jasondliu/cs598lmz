import socket
# Test socket.if_indextoname()

import os
import sys
import unittest
from test import support
from test.support import socket_helper

class IfIndextonameTest(unittest.TestCase):

    def test_if_indextoname(self):
        # Test if_indextoname()
        ifname = socket.if_indextoname(1)
        self.assertIsInstance(ifname, str)
        self.assertGreater(len(ifname), 0)
        self.assertRaises(ValueError, socket.if_indextoname, 0)
        self.assertRaises(OSError, socket.if_indextoname, -1)
        self.assertRaises(OSError, socket.if_indextoname, 65536)

    @unittest.skipUnless(hasattr(socket, 'if_nameindex'),
                         'test needs socket.if_nameindex()')
    def test_if_nameindex(self):
        # Test if_nameindex()
        nameindex = socket.if_nameindex()
        self.assertIs
