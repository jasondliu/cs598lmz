import socket
# Test socket.if_indextoname()

import os, sys
import unittest
import test.test_support

if hasattr(socket, 'if_indextoname'):
    class InterfaceTest(unittest.TestCase):
        def test_if_indextoname(self):
            # On Windows, the loopback interface is named 'Loopback Pseudo-Interface 1'
            # On Linux, the loopback interface is named 'lo'
            self.assertTrue(socket.if_indextoname(1).lower().startswith('loopback'))

        def test_if_indextoname_invalid(self):
            self.assertRaises(ValueError, socket.if_indextoname, -1)
            self.assertRaises(ValueError, socket.if_indextoname, 0)

        def test_if_nameindex(self):
            # On Windows, the loopback interface is named 'Loopback Pseudo-Interface 1'
            # On Linux, the loopback interface is named 'lo'
            self.assertTrue(socket.if_nameindex()[1][1
