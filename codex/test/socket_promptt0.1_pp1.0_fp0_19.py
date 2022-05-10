import socket
# Test socket.if_indextoname()

import unittest
from test import support

class IfIndextonameTest(unittest.TestCase):

    def test_if_indextoname(self):
        # This test is only meaningful on systems that support
        # the SIOCGIFNAME ioctl.
        if not hasattr(socket, 'SIOCGIFNAME'):
            self.skipTest('requires SIOCGIFNAME ioctl')

        # Get the interface associated with the loopback address.
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            ifreq = ioctl(s, socket.SIOCGIFNAME,
                          struct.pack('16sI', b'', socket.INADDR_LOOPBACK))
            loopback_name = ifreq[:16].strip(b'\x00')

        # Test that if_indextoname() returns the same name.
        self.assertEqual(socket.if_indextoname(1), loopback_name)

        # Test that if_indextoname()
