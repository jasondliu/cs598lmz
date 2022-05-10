import socket
# Test socket.if_indextoname
#
# socket.if_indextoname(index)
# Return the name of an interface, given its index.
#
# On error, raises OSError.

import os
import unittest
import errno
from test import support

class IfIndexToNameTest(unittest.TestCase):

    def test_invalid_index(self):
        self.assertRaises(OSError, socket.if_indextoname, 0)
        self.assertRaises(OSError, socket.if_indextoname, 1)
        self.assertRaises(OSError, socket.if_indextoname, -1)
        self.assertRaises(OSError, socket.if_indextoname, -2)
        self.assertRaises(OSError, socket.if_indextoname, -3)
        self.assertRaises(OSError, socket.if_indextoname, -4)

