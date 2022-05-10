import socket
# Test socket.if_indextoname
#
# This test is Linux specific
#
# This test is not included in the standard test suite because it requires
# root privileges to run.
#
# This test is run by the socket_if_indextoname.sh script.

import os
import sys
import unittest
from test import support

if not hasattr(socket, 'if_indextoname'):
    raise unittest.SkipTest("if_indextoname not available")

if os.getuid() != 0:
    raise unittest.SkipTest("need root privileges")


class IfIndextoNameTest(unittest.TestCase):
    def test_if_indextoname(self):
        # get the name of the first interface
        with open('/proc/net/dev', 'r') as f:
            for line in f:
                if ':' in line:
                    name = line.split(':')[0].strip()
                    break
            else:
                self.fail("could not find any interface")
        # get the index of the interface
