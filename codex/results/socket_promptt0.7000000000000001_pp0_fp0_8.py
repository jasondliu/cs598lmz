import socket
# Test socket.if_indextoname(<interface-index>) returns the interface name
# correctly.

import os, sys
import unittest
import errno
import array
import platform

def ifname(i):
    return socket.if_indextoname(i)

class NetworkInterfacesTest(unittest.TestCase):

    def setUp(self):
        if not hasattr(socket, 'if_indextoname'):
            self.skipTest('socket.if_indextoname not available')

    def test_ifname(self):
        # Check ifname(<index>) returns the correct name
        # and that the name is listed in the output of
        # socket.if_nameindex().
        for name, index in socket.if_nameindex():
            self.assertEqual(ifname(index), name)

    def test_ifname_errors(self):
        # Check ifname() raises OverflowError for negative values,
        # TypeError for non-integer arguments and returns None for
        # out of range values.
        for arg in (-1, -2**32, 2
