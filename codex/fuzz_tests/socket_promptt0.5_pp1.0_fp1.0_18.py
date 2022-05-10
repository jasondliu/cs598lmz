import socket
# Test socket.if_indextoname() and socket.if_nametoindex()

import unittest
import sys
import os

from test.support import run_unittest, requires_linux_version

requires_linux_version(2, 2)

class InterfaceTests(unittest.TestCase):

    def test_if_nameindex(self):
        # Test socket.if_nameindex()
        result = socket.if_nameindex()
        self.assertGreater(len(result), 0)
        for idx, name in result:
            self.assertGreater(idx, 0, 'invalid index %r' % idx)
            self.assertTrue(isinstance(name, str),
                            'invalid name %r' % name)

    def test_if_indextoname(self):
        # Test socket.if_indextoname()
        index = socket.if_nametoindex('lo')
        name = socket.if_indextoname(index)
        self.assertEqual(name, 'lo')

    def test_if_nametoindex(
