import socket
# Test socket.if_indextoname(index)

import os, sys
import unittest

class IfIndexToNameTestCase(unittest.TestCase):

    def test_if_indextoname(self):
        if_indextoname = socket.if_indextoname
        if_nametoindex = socket.if_nametoindex
        if_nameindex = socket.if_nameindex

        # Test an interface that is known to exist on all platforms
        name = if_indextoname(1)
        self.assertTrue(if_nametoindex(name) == 1)

        # Test an interface that is known to not exist
        self.assertRaises(OSError, if_indextoname, 0)

        # Test an interface that is known to not exist
        self.assertRaises(ValueError, if_indextoname, -1)

        # Test an interface that is known to not exist
        self.assertRaises(TypeError, if_indextoname, "1")

        # Test an interface that is known to not exist
        self.assertRaises(TypeError
