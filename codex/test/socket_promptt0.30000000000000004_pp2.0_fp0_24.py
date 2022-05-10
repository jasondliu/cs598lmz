import socket
# Test socket.if_indextoname()
#
# This test case is intended to test the socket.if_indextoname() function.
#
# Author: Satoru SATOH <ssato redhat.com>
# License: MIT
#
import os
import os.path
import sys
import unittest

import network_functions_test_utils as NFUT


class Test_if_indextoname(unittest.TestCase):

    def setUp(self):
        self.if_indextoname = NFUT.import_module("if_indextoname")

    def test_10_if_indextoname(self):
        """Test if_indextoname()"""
        if_indextoname = self.if_indextoname.if_indextoname

        self.assertTrue(if_indextoname(1) in ["lo", "lo0"])


if __name__ == '__main__':
    unittest.main()

# vim:sw=4:ts=4:et:
