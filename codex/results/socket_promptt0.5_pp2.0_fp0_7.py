import socket
# Test socket.if_indextoname()
#
# This test is only valid on Linux, and only when run as root.
#
# The test attempts to assign the IP address 127.0.0.1 to each network
# interface on the system, and then checks that if_indextoname() returns
# the correct name for that interface.
#
# The test is not exhaustive, because it is not possible to know which
# interface names are valid on the system.
#
# The test assumes that the system has at least one network interface
# that does not have 127.0.0.1 assigned to it.

import os
import socket
import struct
import sys
import unittest
from test import support
from test.support import import_module

try:
    import fcntl
except ImportError:
    fcntl = None

class IfIndexToNameTest(unittest.TestCase):

    def setUp(self):
        if os.getuid() != 0:
            self.skipTest('test must be run as root')
        if not hasattr(socket, 'if_indextoname'):

