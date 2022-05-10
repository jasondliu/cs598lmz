import socket
# Test socket.if_indextoname()

import socket
import os
import sys
import unittest

from test import support

if not hasattr(socket, 'if_indextoname'):
    raise unittest.SkipTest("if_indextoname not available on this platform")

class IfIndextonameTest(unittest.TestCase):
    def test_if_indextoname(self):
        # Test if_indextoname()
        self.assertEqual(socket.if_indextoname(1), b'lo')
        self.assertEqual(socket.if_indextoname(1, socket.AF_INET), b'lo')
        self.assertEqual(socket.if_indextoname(1, socket.AF_INET6), b'lo')
        self.assertEqual(socket.if_indextoname(1, socket.AF_UNSPEC), b'lo')
        self.assertEqual(socket.if_indextoname(1, socket.AF_INET6,
                                               socket.SOCK_ST
