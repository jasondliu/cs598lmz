import socket
# Test socket.if_indextoname()
#
# The function takes a network interface index and returns the corresponding
# name.
#
# This test is a bit tricky because the interface index is not constant.
# We use a socket to get the interface index of the loopback interface.
#
# The test is skipped if the function is not available.

import socket
import sys
import unittest
from test import support

@unittest.skipUnless(hasattr(socket, "if_indextoname"),
                     "socket.if_indextoname not defined")
class IfIndexToNameTest(unittest.TestCase):

    def test_if_indextoname(self):
        # Get the interface index of the loopback interface.
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(("localhost", 9))
            index = s.getsockopt(socket.SOL_SOCKET, socket.SO_BINDTODEVICE,
                                 4)
        finally:
            s.close()
        # Convert the index
