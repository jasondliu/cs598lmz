import socket
# Test socket.if_indextoname()

import socket
import unittest
from test import support

class IfIndextonameTest(unittest.TestCase):

    def test_if_indextoname(self):
        # Test if_indextoname()
        self.assertRaises(ValueError, socket.if_indextoname, -1)
        self.assertRaises(ValueError, socket.if_indextoname, 0)
        self.assertRaises(ValueError, socket.if_indextoname, 65536)
        self.assertRaises(ValueError, socket.if_indextoname, 65537)

        # Test if_indextoname() with a valid index
        try:
            socket.if_indextoname(1)
        except ValueError:
            # On some platforms, if_indextoname() is not implemented
            # and raises ValueError.
            self.skipTest('if_indextoname() is not implemented')

def test_main():
    support.run_unittest(IfIndextonameTest)


