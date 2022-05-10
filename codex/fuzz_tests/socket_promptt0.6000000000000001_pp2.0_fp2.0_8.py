import socket
# Test socket.if_indextoname()

import unittest
from test.support import run_unittest
from test.support import requires_linux_version

try:
    socket.if_indextoname
except AttributeError:
    # Test not supported on this platform.
    raise unittest.SkipTest("socket.if_indextoname not supported")


def get_index(ifname):
    return socket.if_nametoindex(ifname)


@requires_linux_version(2, 6, 32)
class IfIndextoNameTest(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(socket.if_indextoname(get_index(b'lo')), b'lo')
        self.assertEqual(socket.if_indextoname(get_index(b'eth0')), b'eth0')

    def test_invalid_index(self):
        self.assertRaises(OSError, socket.if_indextoname, -1)
        self.assertRaises(OSError, socket.if
