import socket
# Test socket.if_indextoname()
import socket

import unittest
from test import support

class InterfaceTest(unittest.TestCase):

    def test_if_nameindex(self):
        # The result is a list of (index, name) pairs
        names = socket.if_nameindex()
        self.assertTrue(names)

        # Test the list of pairs for sanity
        for index, name in names:
            self.assertTrue(isinstance(index, int))
            self.assertTrue(isinstance(name, str))
            self.assertEqual(socket.if_indextoname(index), name)
            self.assertEqual(socket.if_nametoindex(name), index)

    def test_if_nameindex_errors(self):
        self.assertRaises(OSError, socket.if_nametoindex, "")
        self.assertRaises(OSError, socket.if_nametoindex, "__spam__")

    def test_if_nameindex_with_too_long_name(self):
        # Issue #22897: if_name
