import socket
# Test socket.if_indextoname()
#
# $Id$
#
#  Copyright (C) 2005   Gregory P. Smith (greg@electricrain.com)
#  Licensed to PSF under a Contributor Agreement.
#

import unittest
from test import test_support

try:
    socket.if_indextoname(1)
except socket.error:
    raise test_support.TestSkipped("No interfaces to test with")

class IfIndexTest(unittest.TestCase):
    def test_if_indextoname(self):
        self.assertTrue(socket.if_indextoname(1))

    def test_if_nametoindex(self):
        self.assertTrue(socket.if_nametoindex(socket.if_indextoname(1)))

def test_main():
    test_support.run_unittest(IfIndexTest)

if __name__ == "__main__":
    test_main()
