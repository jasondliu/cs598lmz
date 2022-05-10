import socket
# Test socket.if_indextoname()

import os
import sys
import unittest
from test import support

if not hasattr(socket, 'if_indextoname'):
    raise unittest.SkipTest("if_indextoname not available")

class IfIndextoNameTest(unittest.TestCase):

    def test_if_indextoname(self):
        # Test if_indextoname()
        self.assertEqual(socket.if_indextoname(1), 'lo')
        self.assertEqual(socket.if_indextoname(2), 'eth0')
        self.assertEqual(socket.if_indextoname(3), 'eth1')
        self.assertEqual(socket.if_indextoname(4), 'sit0')
        self.assertEqual(socket.if_indextoname(5), 'lo')
        self.assertEqual(socket.if_indextoname(6), 'eth0')
        self.assertEqual(socket.if_indextoname(7), 'eth1
