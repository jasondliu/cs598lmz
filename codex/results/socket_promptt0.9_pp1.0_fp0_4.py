import socket
# Test socket.if_indextoname(number) function

#
# Test cases on Fedora Core 5 release
#

import unittest
import os

class If_indextonameTestCase(unittest.TestCase):
    def test_positive01(self):
        """Finding name of a valid if index"""
        index = socket.if_nametoindex("en1")
        self.assertEquals(socket.if_indextoname(index), "en1")

    def test_positive02(self):
        """Finding name of a valid if index"""
        index = socket.if_nametoindex("lo")
        self.assertEquals(socket.if_indextoname(index), "lo")

    def test_positive03(self):
        """Finding name of a valid if index"""
        # Used http://www.fishpool.com/~setok/blog/2004/11/16/\
        # four-ways-to-iterate-over-network-interfaces/ for
        # for loop syntax
        for ifname in sorted(x[1] for x in socket.if_name
