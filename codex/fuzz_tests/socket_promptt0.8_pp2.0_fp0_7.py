import socket
# Test socket.if_indextoname

import os, sys
import unittest
from test.support import is_android
from test.support import run_unittest
import errno

from socket import (
    if_nametoindex, if_indextoname, if_nameindex, if_nametoindex,
    socket, AF_INET, SOCK_DGRAM)

try:
    import fcntl
except ImportError:
    fcntl = None


# We need to test a variant of socket.if_nameindex() that works on the
# current platform and can be called reliably.
try:
    # This variant is used on Mac OS X 10.2 and Tru64
    socket.if_nameindex
    socket.if_indextoname
    socket.if_nametoindex
    def if_nameindex():
        return [(i, socket.if_indextoname(i)) for i in socket.if_nameindex()]

    def test_if_nameindex():
        """Test 'socket.if_nameindex'"""
        # This should work on any platform with a
