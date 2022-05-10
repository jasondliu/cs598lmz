import socket
# Test socket.if_indextoname()

from test import support
import unittest

class IfIndextonameTestCase(unittest.TestCase):

    def test_if_indextoname(self):
        # Test if_indextoname()
        self.assertRaises(OverflowError, socket.if_indextoname, 2**32)
        self.assertRaises(OverflowError, socket.if_indextoname, -1)
        self.assertRaises(ValueError, socket.if_indextoname, 0)
        self.assertRaises(ValueError, socket.if_indextoname, 1)
        self.assertRaises(ValueError, socket.if_indextoname, 2)

        # Test if_indextoname() with a valid interface index
        try:
            socket.if_indextoname(3)
        except ValueError:
            # On Windows, the interface index must be greater than or equal to
            # 1.
            if support.platform != 'win32':
                raise

