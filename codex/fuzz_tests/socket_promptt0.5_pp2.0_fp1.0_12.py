import socket
# Test socket.if_indextoname()
#
# This test checks if socket.if_indextoname() returns the correct interface
# name for a given interface index.

import unittest
import socket
import os
import errno

from test import support


class InterfaceTestCase(unittest.TestCase):

    def test_if_indextoname(self):
        # Get the list of all available interfaces.
        ifaces = os.listdir('/sys/class/net/')
        for iface in ifaces:
            # Get the interface index of the interface.
            fd = os.open('/sys/class/net/' + iface + '/ifindex', os.O_RDONLY)
            ifindex = os.read(fd, 1024)
            os.close(fd)

            # Check if the interface name is returned correctly.
            ifname = socket.if_indextoname(int(ifindex))
            self.assertEqual(ifname, iface)

    def test_if_indextoname_invalid(self):
        # Check if an exception is raised
