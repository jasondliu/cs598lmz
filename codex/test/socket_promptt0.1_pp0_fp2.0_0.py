import socket
# Test socket.if_indextoname()

import unittest
import socket
import os
import sys
import errno
import platform

from test import support

if not hasattr(socket, 'if_indextoname'):
    raise unittest.SkipTest("socket.if_indextoname not defined")

if platform.system() == 'Windows':
    raise unittest.SkipTest("Windows does not support if_indextoname")

class IfIndextonameTest(unittest.TestCase):

    def test_if_indextoname(self):
        # Test if_indextoname()
        self.assertEqual(socket.if_indextoname(1), 'lo')

    def test_if_indextoname_error(self):
        # Test if_indextoname() errors
        self.assertRaises(OverflowError, socket.if_indextoname, -1)
        self.assertRaises(OverflowError, socket.if_indextoname, 2**32)
