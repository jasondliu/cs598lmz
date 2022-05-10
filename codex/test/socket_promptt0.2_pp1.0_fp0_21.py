import socket
# Test socket.if_indextoname()
#
# This test is intended to check the functionality of the socket.if_indextoname()
# method.
#
# Author: Satoru SATOH <ssato redhat.com>
# License: MIT
#
import os
import os.path
import sys
import unittest


class Test_if_indextoname(unittest.TestCase):

    def test_if_indextoname(self):
        if os.path.exists("/sys/class/net/lo"):
            self.assertEquals(socket.if_indextoname(1), "lo")
        else:
            self.assertEquals(socket.if_indextoname(1), "lo0")


# vim:sw=4:ts=4:et:
