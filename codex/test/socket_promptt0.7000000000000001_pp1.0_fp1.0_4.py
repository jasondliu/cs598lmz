import socket
# Test socket.if_indextoname() and socket.if_nametoindex()

import os, sys
import unittest
from test import support

support.requires('network')

if not hasattr(socket, "if_indextoname"):
    raise unittest.SkipTest("if_indextoname not available on this platform")
if not hasattr(socket, "if_nametoindex"):
    raise unittest.SkipTest("if_nametoindex not available on this platform")

class InterfaceTest(unittest.TestCase):

    def test_if_indextoname(self):
        # Test if_indextoname()
        # returns the interface name for a given interface index
        with support.EnvironmentVarGuard() as env:
            env['IF_NAMESIZE'] = str(256)
            self.assertEqual(socket.if_indextoname(1), b'lo')

        # Test for error conditions
        with self.assertRaises(ValueError):
            socket.if_indextoname(-1)
