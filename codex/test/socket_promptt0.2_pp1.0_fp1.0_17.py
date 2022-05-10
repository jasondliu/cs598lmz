import socket
# Test socket.if_indextoname()

import os
import sys
import unittest
from test import support

if_indextoname = socket.if_indextoname

class IfIndextoNameTest(unittest.TestCase):

    def test_if_indextoname(self):
        # Test if_indextoname()
        self.assertRaises(ValueError, if_indextoname, -1)
        self.assertRaises(ValueError, if_indextoname, 0)
        self.assertRaises(ValueError, if_indextoname, 1)
        self.assertRaises(ValueError, if_indextoname, 2)
        self.assertRaises(ValueError, if_indextoname, 3)
        self.assertRaises(ValueError, if_indextoname, 4)
        self.assertRaises(ValueError, if_indextoname, 5)
        self.assertRaises(ValueError, if_indextoname, 6)
