import socket
# Test socket.if_indextoname()

import os
import sys
import unittest
from test import support

if not hasattr(socket, 'if_indextoname'):
    raise unittest.SkipTest("if_indextoname not defined")

class IfIndextonameTest(unittest.TestCase):

    def test_if_indextoname(self):
        # On Windows, if_indextoname() is only available on Vista and later.
        if sys.platform == 'win32' and sys.getwindowsversion()[:2] < (6, 0):
            self.assertRaises(OSError, socket.if_indextoname, 0)
        else:
            self.assertIsInstance(socket.if_indextoname(0), str)

    def test_if_indextoname_errors(self):
        self.assertRaises(OverflowError, socket.if_indextoname, -1)
        self.assertRaises(OverflowError, socket.if_indextoname, 2**32)
