import socket
# Test socket.if_indextoname()

import os
import sys
import unittest
import socket

from test import support
from test.support import import_module

# Skip test if there is no network interface on this machine
socket = import_module('socket')
try:
    socket.if_indextoname(1)
except OSError:
    raise unittest.SkipTest("No network interface on this machine")

class IfIndextonameTest(unittest.TestCase):

    def test_if_indextoname(self):
        name = socket.if_indextoname(1)
        self.assertTrue(name)

    def test_if_indextoname_invalid_index(self):
        self.assertRaises(OSError, socket.if_indextoname, -1)
        self.assertRaises(OSError, socket.if_indextoname, 0)
        self.assertRaises(OSError, socket.if_indextoname, 65536)

