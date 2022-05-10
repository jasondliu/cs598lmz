import socket
# Test socket.if_indextoname()

import unittest
from test import support
from test.support import import_module

# Skip test if _socket doesn't exist
socket = import_module('_socket')

class TestIfIndextoname(unittest.TestCase):

    def test_if_indextoname(self):
        # Test if_indextoname()
        ifname = socket.if_indextoname(1)
        self.assertTrue(isinstance(ifname, str))

    def test_error_conditions(self):
        # Test if_indextoname() for error conditions
        self.assertRaises(OverflowError, socket.if_indextoname, 2**32)
        self.assertRaises(OSError, socket.if_indextoname, -1)
        self.assertRaises(OSError, socket.if_indextoname, 0)

    def test_invalid_args(self):
        # Test if_indextoname() for invalid arguments
        self.assertRaises(TypeError, socket.if_indexton
