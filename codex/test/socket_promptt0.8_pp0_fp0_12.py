import socket
# Test socket.if_indextoname()
#
# This needs an interface with an IPv6 address.
#
# IPv6 test disabled since it doesn't work with Windows TAP adapter.
#
# From reading the code, it looks to me that the intent was to pass the
# interface index in to if_indextoname(). This works on Linux, but not
# on Windows.
#
# On Windows, the BSD socket API returns the index number of the interface
# as the name, so this test only works if the interface name is numeric.

import unittest
from test import support
import socket

nonet = False

try:
    socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
except OSError:
    nonet = "IPv6 is not supported"

