import socket
# Test socket.if_indextoname' function.

import unittest
import os

import test.support
from test.support import TESTFN, find_unused_port

try:
    socket.if_indextoname
except AttributeError:
    raise unittest.SkipTest("Platform doesn't support socket.if_indextoname")

class InterfaceIndexNamesTest(unittest.TestCase):

    def test_if_indextoname(self):
        name = socket.if_indextoname(1)
        self.assertTrue(name)

    def test_if_indextoname_errors(self):
        self.assertRaises(OSError, socket.if_indextoname, 0)
        self.assertRaises(OSError, socket.if_indextoname, -1)
        self.assertRaises(OverflowError, socket.if_indextoname, 2**31)
        self.assertRaises(OverflowError, socket.if_indextoname, -2**31)

