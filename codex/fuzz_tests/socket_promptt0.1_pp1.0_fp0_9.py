import socket
# Test socket.if_indextoname()

import unittest
from test import support

class IfIndextonameTest(unittest.TestCase):

    def test_if_indextoname(self):
        # Test if_indextoname()
        self.assertRaises(ValueError, socket.if_indextoname, -1)
        self.assertRaises(ValueError, socket.if_indextoname, 0)
        self.assertRaises(ValueError, socket.if_indextoname, 1)
        self.assertRaises(ValueError, socket.if_indextoname, 2)
        self.assertRaises(ValueError, socket.if_indextoname, 3)
        self.assertRaises(ValueError, socket.if_indextoname, 4)
        self.assertRaises(ValueError, socket.if_indextoname, 5)
        self.assertRaises(ValueError, socket.if_indextoname, 6)
        self.assertRaises(ValueError, socket.if_indextoname, 7)
       
