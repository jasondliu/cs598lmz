import socket
# Test socket.if_indextoname()

import sys, os
import unittest
from test import support

class IfIndextonameTest(unittest.TestCase):

    def test_if_indextoname(self):
        # Issue #7995: if_indextoname() should return None if the index is
        # invalid.
        self.assertIsNone(socket.if_indextoname(0))
        self.assertIsNone(socket.if_indextoname(-1))
        self.assertIsNone(socket.if_indextoname(1 << 32))

    @unittest.skipUnless(hasattr(socket, 'if_nameindex'), 'need if_nameindex')
    def test_if_indextoname_nameindex(self):
        # Issue #7995: if_indextoname() should return the same name as
        # if_nameindex() for valid indices.
        for index, name in socket.if_nameindex():
            self.assertEqual(socket.if_indextoname(index), name)

    @unittest.skip
