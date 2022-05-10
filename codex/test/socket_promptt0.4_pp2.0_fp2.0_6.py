import socket
# Test socket.if_indextoname()

import os
import sys
import unittest
from test import support
from test.support import import_module

try:
    import_module('fcntl')
except ImportError:
    raise unittest.SkipTest("fcntl module not available")

import fcntl
import socket

class IfIndexToNameTest(unittest.TestCase):
    def test_if_indextoname(self):
        # Test if_indextoname()
        try:
            ifname = socket.if_indextoname(1)
        except OSError as err:
            if err.errno == errno.ENXIO:
                # No such network interface
                self.skipTest("No network interface found")
            raise
        self.assertIsInstance(ifname, str)
        self.assertTrue(ifname)

