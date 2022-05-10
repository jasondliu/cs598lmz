import socket
# Test socket.if_indextoname

import unittest
from test import test_support
import socket

class IfIndextonameTest(unittest.TestCase):
    def test_ifindextoname(self):
        try:
            name = socket.if_indextoname(1)
        except OSError:
            # On some platforms, there is no interface with index 1,
            # so we can't really test anything else.
            pass
        else:
            self.assertTrue(name)
            self.assertEqual(socket.if_indextoname(1), name)
            self.assertTrue(socket.if_nametoindex(name))

    def test_ifindextoname_errors(self):
        self.assertRaises(OSError, socket.if_indextoname, -1)
        self.assertRaises(OSError, socket.if_indextoname, 0)
        self.assertRaises(OSError, socket.if_indextoname, 99999)

