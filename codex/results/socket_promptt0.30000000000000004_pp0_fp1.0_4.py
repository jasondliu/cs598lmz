import socket
# Test socket.if_indextoname()

import os
import sys
import unittest
from test import support

if not hasattr(socket, 'if_indextoname'):
    raise unittest.SkipTest("socket.if_indextoname not defined")

class InterfaceTest(unittest.TestCase):
    def test_if_indextoname(self):
        # The index should be valid
        try:
            ifname = socket.if_indextoname(1)
        except OSError as e:
            self.assertEqual(e.errno, errno.EINVAL)
        else:
            self.assertIsInstance(ifname, str)
            self.assertGreater(len(ifname), 0)

    def test_if_indextoname_invalid_index(self):
        # The index should be invalid
        self.assertRaises(OSError, socket.if_indextoname, 0xffffffff)

    def test_if_indextoname_errors(self):
        # The index should be invalid
        self.assert
