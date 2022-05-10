import socket
# Test socket.if_indextoname()
import unittest
import os
from test.support import import_module
from test import support, socket_helper, os_helper


try:
    if_indextoname = socket.if_indextoname
except AttributeError:
    raise unittest.SkipTest(
        "{}.if_indextoname is not available".format(__name__))


class IfIndextoNameTest(unittest.TestCase):

    def testInvalidName(self):
        # https://github.com/python/cpython/issues/2707
        if_indextoname(1)
        # Non-positive index raises ValueError
        with self.assertRaises(ValueError):
            if_indextoname(0)
        # Negative index raises OverflowError on Windows
        with self.assertRaises(OverflowError):
            if_indextoname(-1)


class InetAddrTest(unittest.TestCase):

    def testBug810615(self):
        import socket
