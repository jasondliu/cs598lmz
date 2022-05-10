import socket
# Test socket.if_indextoname()

import os
import sys
import unittest
from test import support

# Skip test if if_indextoname() is not available
if not hasattr(socket, 'if_indextoname'):
    raise unittest.SkipTest("if_indextoname() not available")

# Skip test if the interface name is too long for the platform
ifname = socket.if_indextoname(1)
if len(ifname) >= support.IFNAMSIZ:
    raise unittest.SkipTest("interface name too long for platform")

class InterfaceTest(unittest.TestCase):

    def test_error_conditions(self):
        # invalid arguments
        self.assertRaises(OverflowError, socket.if_indextoname, 1<<32)
        self.assertRaises(OverflowError, socket.if_indextoname, -1)
        self.assertRaises(TypeError, socket.if_indextoname)

        # non-existent interface
        self.assertRaises(OSError, socket.if_
