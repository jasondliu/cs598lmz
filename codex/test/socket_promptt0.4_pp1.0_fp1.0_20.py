import socket
# Test socket.if_indextoname

import test.support
import unittest
import sys
import os

if_indextoname = socket.if_indextoname
if_nametoindex = socket.if_nametoindex

class IfNameToIndexTest(unittest.TestCase):

    def test_if_indextoname(self):
        self.assertRaises(OverflowError, if_indextoname, 2**32)
        self.assertRaises(OverflowError, if_indextoname, -1)
        self.assertRaises(OSError, if_indextoname, 0)
        self.assertRaises(OSError, if_indextoname, 1)

    def test_if_nametoindex(self):
        self.assertRaises(OSError, if_nametoindex, "")
        self.assertRaises(OSError, if_nametoindex, "a"*256)

