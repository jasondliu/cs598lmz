import socket
# Test socket.if_indextoname()

import unittest
from test import support

class IfIndextonameTest(unittest.TestCase):

    def test_if_indextoname(self):
        # Test if_indextoname()
        if_indextoname = socket.if_indextoname
        self.assertRaises(ValueError, if_indextoname, -1)
        self.assertRaises(ValueError, if_indextoname, 0)
        self.assertRaises(ValueError, if_indextoname, 256)
        self.assertRaises(ValueError, if_indextoname, 2**32)
        self.assertRaises(ValueError, if_indextoname, 2**64)
        self.assertRaises(TypeError, if_indextoname, None)
        self.assertRaises(TypeError, if_indextoname, 'a')
        self.assertRaises(TypeError, if_indextoname, 1.5)
