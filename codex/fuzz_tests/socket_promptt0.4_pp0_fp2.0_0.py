import socket
# Test socket.if_indextoname()

import unittest
from test import support

class IfIndextoNameTest(unittest.TestCase):

    def test_if_indextoname(self):
        # Try to find a valid interface name.
        # This is not the best way to do this, but it's portable.
        # We could use SIOCGIFCONF, but that's not portable.
        # We could use netifaces, but that's not in the stdlib.
        # We could use ifconfig -a, but that's not portable.
        # We could use getifaddrs, but that's not in the stdlib.
        # We could use netstat -i, but that's not portable.
        # We could use netstat -g, but that's not portable.
        # We could use netsh, but that's not portable.
        # We could use WMI, but that's not portable.
        # We could use a registry key, but that's not portable.
        # We could use GetAdaptersAddresses, but that's not portable.
        # We could use GetIfTable,
