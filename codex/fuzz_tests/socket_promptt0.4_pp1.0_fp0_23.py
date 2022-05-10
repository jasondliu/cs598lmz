import socket
# Test socket.if_indextoname()
import sys
import unittest

from test import support
from test.support import import_module

@unittest.skipUnless(hasattr(socket, 'if_indextoname'),
                     'test needs socket.if_indextoname()')
class IfIndextoNameTest(unittest.TestCase):
    @unittest.skipUnless(hasattr(socket, 'if_nameindex'),
                         'test needs socket.if_nameindex()')
    def test_if_indextoname(self):
        # This test is Linux specific.  It assumes that the first interface
        # has index 1.  It also assumes that the first interface name is
        # 'lo'.
        name = socket.if_indextoname(1)
        self.assertEqual(name, 'lo')

    def test_invalid_index(self):
        self.assertRaises(OSError, socket.if_indextoname, -1)
        self.assertRaises(OSError, socket.if_indextoname, 0)
        self.assert
