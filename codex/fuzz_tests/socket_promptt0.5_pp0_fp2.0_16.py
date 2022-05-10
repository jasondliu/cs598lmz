import socket
# Test socket.if_indextoname()
#
# This test is Linux specific
#
# This test will fail if the Python interpreter is not build with IPv6
# support.
#
# This test will fail if the platform does not support IPv6.
#
# This test will fail if the platform does not have a network interface.

import unittest
from test import support
import socket
import sys
if not hasattr(socket, "if_indextoname"):
    raise support.TestSkipped("socket module has no if_indextoname()")

try:
    socket.if_indextoname(1)
except Exception as msg:
    raise support.TestSkipped(
        "if_indextoname() not supported by this platform: %s" % msg)

class IfIndextoNameTest(unittest.TestCase):

    def test_if_indextoname(self):
        try:
            socket.if_indextoname(1)
        except OSError:
            # No network interface available
            return
        if sys.platform.startswith('linux'
