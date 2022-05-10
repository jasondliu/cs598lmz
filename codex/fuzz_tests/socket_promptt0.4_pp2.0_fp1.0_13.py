import socket
# Test socket.if_indextoname()

import os
import sys
import unittest
from test import support

try:
    socket.if_indextoname
except AttributeError:
    raise unittest.SkipTest("if_indextoname not supported")


class IfIndextonameTest(unittest.TestCase):

    def test_if_indextoname(self):
        # Check that if_indextoname() returns a valid interface name
        # for all valid interface indexes.
        for i in range(256):
            name = socket.if_indextoname(i)
            if name is not None:
                self.assertEqual(i, socket.if_nametoindex(name))

    def test_if_indextoname_invalid_index(self):
        # Check that if_indextoname() raises OSError for an invalid
        # interface index.
        with self.assertRaises(OSError):
            socket.if_indextoname(256)


def test_main():
    support.run_unittest(IfInd
