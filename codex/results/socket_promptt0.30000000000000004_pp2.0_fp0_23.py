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
        ifname = socket.if_indextoname(1)
        if not ifname:
            raise unittest.SkipTest("if_indextoname() returned empty string")
        self.assertEqual(type(ifname), str)
        self.assertTrue(ifname)

    def test_if_indextoname_invalid_index(self):
        # Test if_indextoname() with invalid index
        self.assertRaises(ValueError, socket.if_indextoname, -1)
        self.assertRaises(ValueError, socket.if_indextoname, 0)
        self.assertRaises(OSError,
