import socket
# Test socket.if_indextoname(), socket.getaddrinfo() and socket.getnameinfo() with
# the IPv6 localhost

import test.test_support
import unittest

class LocalhostIPv6Test(unittest.TestCase):

    def test_if_indextoname(self):
        # Check if IPv6 localhost works
        self.assertEqual(socket.if_indextoname(1, socket.AF_INET6),
                         '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01')

    def test_getaddrinfo(self):
        # Check if IPv6 localhost works for getaddrinfo
        result = socket.getaddrinfo('ipv6-localhost', None)
        self.assertEqual(result[0][0], socket.AF_INET6)
