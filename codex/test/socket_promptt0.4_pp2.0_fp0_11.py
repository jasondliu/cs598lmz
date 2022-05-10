import socket
# Test socket.if_indextoname()

import sys
import os
import unittest
import socket
from test import support
from test.support import find_unused_port

class IfIndexToNameTest(unittest.TestCase):
    def test_if_indextoname(self):
        # This test only works on Linux, because it requires a network
        # interface to be present.
        if not sys.platform.startswith('linux'):
            raise unittest.SkipTest("Linux only")
        # Find the first interface name.
        f = os.popen('/sbin/ifconfig -a', 'r')
        try:
            for line in f:
                if 'Link encap:' in line:
                    ifname = line.split()[0]
                    break
            else:
                self.fail("Could not find an interface name")
        finally:
            f.close()
        # Find the index corresponding to that name.
        f = os.popen('/sbin/ifconfig -a', 'r')
