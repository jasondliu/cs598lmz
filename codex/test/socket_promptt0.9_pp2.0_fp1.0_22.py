import socket
# Test socket.if_indextoname()

import unittest
from test import support
import _socket

# Test various supported platforms
try:
    _socket.if_indextoname(1)
    HAVE_IFINDEXTONAME = True
except Exception:
    HAVE_IFINDEXTONAME = False

if HAVE_IFINDEXTONAME:
    class TestIfIndextoname(unittest.TestCase):
        def test_if_indextoname(self):
            format = "%%-%us" % _socket.IFNAMSIZ
            for ifname in _socket.if_nameindex():
                self.assertEqual(ifname[1], format % _socket.if_indextoname(ifname[0]))

    class TestIfNametoIndex(unittest.TestCase):
        def test_if_nametoindex(self):
            for ifname in _socket.if_nameindex():
                self.assertEqual(ifname[0], _socket.if_nametoindex(ifname[1]))

