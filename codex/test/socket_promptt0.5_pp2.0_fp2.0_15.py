import socket
# Test socket.if_indextoname(index)

import os
import sys
import unittest
from test import support
from socket import AF_INET, AF_INET6

class TestIf_indextoname(unittest.TestCase):

    def test_if_indextoname(self):
        # Test socket.if_indextoname(index)
        try:
            socket.if_indextoname(1)
        except Exception as msg:
            self.fail("socket.if_indextoname(1) failed with error: %s" % msg)

        try:
            socket.if_indextoname(-1)
        except ValueError as msg:
            self.assertIn("invalid literal for int()", str(msg))
        except Exception as msg:
            self.fail("socket.if_indextoname(-1) failed with error: %s" % msg)

        try:
            socket.if_indextoname(1.0)
        except ValueError as msg:
            self.assertIn("invalid literal for int()", str(msg))

