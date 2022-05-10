import socket
# Test socket.if_indextoname on Linux
import unittest
import sys
from test import test_support

class InterfaceTest(unittest.TestCase):
    def test_if_nameindex(self):
        # Issue #1764: segfault if the interface name is too long
        # (the name should be truncated)
        self.assertEqual(len(socket.if_nameindex()),
                         len(socket.if_nameindex()))

    def test_if_nametoindex(self):
        # Issue #1764: segfault if the interface name is too long
        # (the name should be truncated)
        self.assertEqual(socket.if_nametoindex('lo'), 1)
        self.assertRaises(OSError, socket.if_nametoindex, 'does-not-exist')

    def test_if_indextoname(self):
        # Issue #1764: segfault if the interface name is too long
        # (the name should be truncated)
        self.assertEqual(socket.if_indextoname(1), '
