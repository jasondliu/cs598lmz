import socket
# Test socket.if_indextoname()
#
# This test case checks the basic functionality of the
# socket.if_indextoname() function.
#
# Author: S. Thiell
# $Id: test_if_indextoname.py,v 1.2 2004/02/20 19:16:04 mjp Exp $

import unittest
import socket

class IfIndexToNameTest(unittest.TestCase):
    def test_if_indextoname(self):
        # check that we can get the interface name for a valid index
        ifname = socket.if_indextoname(1)
        if ifname is None:
            self.fail("socket.if_indextoname() returned None")
        # check that we get None for a bogus index
        ifname = socket.if_indextoname(9999)
        if ifname is not None:
            self.fail("socket.if_indextoname() returned a non-None value")

def test_main():
    suite = unittest.TestSuite()
