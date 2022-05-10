import socket
# Test socket.if_indextoname()
# This is a convenience function that combines the steps of calling
# socket.if_nameindex() and socket.if_indextoname() to get the interface
# name from an interface index.

import os
import unittest
from test import support
from test.support import os_helper

def safe_if_indextoname(n):
    try:
        return socket.if_indextoname(n)
    except OSError:
        return None

class IfIndextoNameTest(unittest.TestCase):

    def test_known_index(self):
        # Iterate over all known interfaces, and check that if_indextoname()
        # returns the correct name for known indices.
        for name, index in socket.if_nameindex():
            self.assertEqual(name, safe_if_indextoname(index))
        # Test a few known indices with known names.
        if os_helper.TEST_DEFAULT_INTERFACE_INDEX_AND_NAME:
            index, name = os_helper.T
