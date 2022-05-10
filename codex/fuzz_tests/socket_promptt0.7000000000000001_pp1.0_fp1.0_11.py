import socket
# Test socket.if_indextoname() function

import os
import sys
import unittest
import socket
from test import support

import test.support

class IfIndextonameTestCase(unittest.TestCase):

    def test_if_indextoname(self):
        # Test a valid index
        with support.detach_socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            ifname = socket.if_indextoname(s.getsockopt(socket.SOL_SOCKET,
                socket.SO_BINDTODEVICE))
        self.assertTrue(ifname)

    @unittest.skipUnless(hasattr(socket, 'if_nameindex'),
                         'test needs socket.if_nameindex()')
    def test_if_indextoname_with_invalid_index(self):
        # Try to test an invalid index
        if_nameindex = socket.if_nameindex()
        # find a free index and test it
        index = 1
        while True:
            if index not in [x[0
