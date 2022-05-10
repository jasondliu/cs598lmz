import socket
# Test socket.if_indextoname()
import sys

import test.support
import unittest

if not hasattr(socket, 'if_indextoname'):
    raise unittest.SkipTest('if_indextoname() not available')


class TestIPv6(unittest.TestCase):

    def test_if_indextoname(self):
        for name in socket.if_nameindex():
            try:
                socket.if_indextoname(name[0])
            except OSError:
                continue

    def test_if_nametoindex(self):
        for name in socket.if_nameindex():
            try:
                socket.if_nametoindex(name[1])
            except OSError:
                continue

    def test_if_nameindex(self):
        socket.if_nameindex()

