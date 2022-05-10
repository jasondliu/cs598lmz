import socket
# Test socket.if_indextoname()

# Test socket.if_indextoname()

import os
import sys
import unittest
import socket

from test import support

class InterfaceTest(unittest.TestCase):

    def test_if_indextoname(self):
        # Test socket.if_indextoname()
        if_indextoname = socket.if_indextoname
        self.assertRaises(OverflowError, if_indextoname, 2**32)
        self.assertRaises(OverflowError, if_indextoname, -1)
        self.assertRaises(OSError, if_indextoname, 0)
        self.assertRaises(OSError, if_indextoname, 1)
        self.assertRaises(OSError, if_indextoname, 2)
        self.assertRaises(OSError, if_indextoname, 3)
        self.assertRaises(OSError, if_indextoname, 4)
        self.assertRaises(OSError, if_indextoname,
