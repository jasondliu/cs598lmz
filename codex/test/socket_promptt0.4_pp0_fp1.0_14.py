import socket
# Test socket.if_indextoname()

from test import support
import unittest

class IfIndexToNameTest(unittest.TestCase):
    def test_if_indextoname(self):
        # This test is only useful on systems that support the SIOCGIFNAME ioctl.
        if not hasattr(socket, 'SIOCGIFNAME'):
            self.skipTest('SIOCGIFNAME ioctl not supported')

        # Create a dummy socket and get its interface index.
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        ifname = socket.if_indextoname(s.getsockopt(socket.SOL_SOCKET,
                                                    socket.SO_BINDTODEVICE))

        # Check that if_indextoname() returns the correct name for the
        # interface index.
        self.assertEqual(socket.if_indextoname(s.getsockopt(socket.SOL_SOCKET,
                                                            socket.SO_BINDTODEVICE)),
                         ifname)

       
