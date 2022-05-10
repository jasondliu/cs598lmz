import socket
# Test socket.if_indextoname()

import socket
import unittest
from test import support
from test.support import os_helper

if_indextoname = socket.if_indextoname

class IfIndextonameTest(unittest.TestCase):

    def test_errors(self):
        self.assertRaises(OverflowError, if_indextoname, 2**32)
        self.assertRaises(OSError, if_indextoname, -1)

    @unittest.skipUnless(hasattr(socket, 'if_nametoindex'),
                         'test needs socket.if_nametoindex()')
    def test_roundtrip(self):
        # Test that if_indextoname() and if_nametoindex() are inverses.
        for name in socket.if_nameindex():
            index = name[0]
            name = name[1]
            if not name:
                continue
            try:
                self.assertEqual(name, if_indextoname(index))
            except OSError:
                # On some
