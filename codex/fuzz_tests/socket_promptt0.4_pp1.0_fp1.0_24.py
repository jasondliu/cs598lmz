import socket
# Test socket.if_indextoname()

import os
import sys
import unittest
from test import support

if_indextoname = support.import_module('socket').if_indextoname

class TestIfIndextoName(unittest.TestCase):

    @unittest.skipUnless(hasattr(socket, 'if_indextoname'),
                         'test needs socket.if_indextoname()')
    def test_if_indextoname(self):
        # This test is only meaningful on systems that support at least
        # one network interface
        ifname = if_indextoname(1)
        self.assertTrue(ifname is not None,
                        "couldn't find interface with index 1")
        self.assertIsInstance(ifname, str)
        self.assertGreater(len(ifname), 0)

    @unittest.skipUnless(hasattr(socket, 'if_indextoname'),
                         'test needs socket.if_indextoname()')
    def test_if_indextoname_errors(self):
        # This
