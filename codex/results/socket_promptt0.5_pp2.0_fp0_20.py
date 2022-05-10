import socket
# Test socket.if_indextoname
#
# if_indextoname() should return the interface name for a given interface
# index.

import os, sys
import unittest
from test import test_support

class IfIndexToNameTest(unittest.TestCase):

    def test_if_indextoname(self):
        # Get the list of valid interfaces
        valid_ifaces = []
        with os.popen('/sbin/ifconfig -a', 'r') as f:
            for line in f:
                if line.startswith('\t'):
                    continue
                valid_ifaces.append(line.split()[0])

        # Check that if_indextoname() returns the right interface name
        # for each interface index.
        for ifname in valid_ifaces:
            index = socket.if_nametoindex(ifname)
            self.assertEqual(ifname, socket.if_indextoname(index))

def test_main():
    test_support.run_unittest(IfIndexToNameTest)

if __name__
