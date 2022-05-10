import socket
# Test socket.if_indextoname()

import unittest
import os
import sys
import errno
import socket
import array
import struct
import fcntl
import platform

from test import test_support

if not hasattr(socket, 'if_indextoname'):
    raise test_support.TestSkipped("if_indextoname not available")

class IfIndextonameTest(unittest.TestCase):
    def setUp(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def tearDown(self):
        self.sock.close()

    def test_if_indextoname(self):
        # Get the list of interfaces
        names = socket.if_nameindex()
        # Test each interface
        for if_index, if_name in names:
            self.assertEqual(socket.if_indextoname(if_index), if_name)

    def test_if_indextoname_invalid_index(self):
        # Test invalid index
        self
