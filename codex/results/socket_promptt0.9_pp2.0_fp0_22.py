import socket
# Test socket.if_indextoname on Linux.

import socket
import unittest

from test import test_support

try:
    socket.if_indextoname(1)
except ValueError: # bpo-34984: Netlink interface IDs must be positive
    raise unittest.SkipTest("test skips with Netlink interface IDs must be positive")

class InterfaceTest(unittest.TestCase):

    def testNoGood(self):
        self.assertRaises(ValueError, socket.if_indextoname, -1)
        self.assertRaises(ValueError, socket.if_indextoname, 'ham')
        self.assertRaises(ValueError, socket.if_indextoname, None)

    def testRecovery(self):
        try:
            socket.if_indextoname(socket.if_nametoindex('lo'))
        except socket.error, msg:
            if m
