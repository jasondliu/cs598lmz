import socket
# Test socket.if_indextoname() (& socket.if_nametoindex())
# This test is not thorough.  Add more cases as seen fit.
import socket
import unittest

from test import support

class InterfaceTest(unittest.TestCase):
    def testName(self):
        # For every interface index, if_indextoname() should be able to map
        # back to the same name.
        #
        # Earlier versions of this test started with index 1 and checked the
        # first 64 indexes.  This is not sufficient to test the mapping is
        # correct.  The last interface name on my test Windows machine was
        # "Broadcom NetXtreme #2".  This has an index of 77, and my 64th
        # interface has an index of 21.  Thus, starting with 1 would have
        # given me a false positive.  This could happen on any system with a
        # large number of interfaces, even if the indexes were not sparse.
        for i in range(256):
            try:
                name = socket.if_indextoname(i)
            except OSError:

