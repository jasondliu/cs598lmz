import socket
# Test socket.if_indextoname()

import os, sys
from test_support import run_unittest, import_module, requires

requires('network')
_netifaces = import_module('netifaces')

from socket import htons, AF_INET, AF_INET6, inet_pton

TEST_IFACE = 'lo'
TEST_ADDRESS = ('127.0.0.1', '::1')

@unittest.skipUnless(sys.platform.startswith("linux"),
                     "if_indextoname() is only supported on Linux.")
class IfIndextonameTest(TestCase):
    def setUp(self):
        if socket.if_nametoindex(TEST_IFACE) == 0:
            self.skipTest('%s interface not found' % TEST_IFACE)

