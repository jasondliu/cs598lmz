import socket
# Test socket.if_indextoname()

import unittest
from test import support

class IfIndextonameTestCase(unittest.TestCase):

    def test_if_indextoname(self):
        # Issue #9233: if_indextoname() should not crash on invalid index.
        self.assertRaises(ValueError, socket.if_indextoname, -1)
        self.assertRaises(ValueError, socket.if_indextoname, 0)
        self.assertRaises(ValueError, socket.if_indextoname, 1<<32)
        self.assertRaises(ValueError, socket.if_indextoname, 1<<64)

        # Issue #9233: if_indextoname() should not crash on invalid index.
        self.assertRaises(ValueError, socket.if_indextoname, -1)
        self.assertRaises(ValueError, socket.if_indextoname, 0)
        self.assertRaises(ValueError, socket.if_indextoname, 1<<32)
        self.assert
