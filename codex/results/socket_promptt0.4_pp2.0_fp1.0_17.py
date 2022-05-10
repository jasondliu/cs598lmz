import socket
# Test socket.if_indextoname()
import sys
import unittest

from test import support

if not hasattr(socket, 'if_indextoname'):
    raise unittest.SkipTest('if_indextoname not available')

if sys.platform == 'darwin':
    raise unittest.SkipTest('if_indextoname not working on macOS')


class IfIndexToNameTest(unittest.TestCase):
    def test_if_indextoname(self):
        self.assertEqual(socket.if_indextoname(1), 'lo')

    def test_if_indextoname_invalid(self):
        self.assertRaises(ValueError, socket.if_indextoname, 0)

    def test_if_indextoname_unknown(self):
        self.assertRaises(ValueError, socket.if_indextoname, 0xffffffff)


class IfNameToIndexTest(unittest.TestCase):
    def test_if_nametoindex(self):
        self.assertEqual(socket.
