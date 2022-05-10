import socket
# Test socket.if_indextoname()

import sys
import unittest
from test import support
from test.support import os_helper

if not hasattr(socket, 'if_indextoname'):
    raise unittest.SkipTest("if_indextoname not available")

class IfIndextonameTest(unittest.TestCase):

    def test_if_indextoname(self):
        # Test if_indextoname()
        # Get the list of network interfaces
        with os_helper.temp_dir() as td:
            with open(os.path.join(td, 'ifconfig.out'), 'w') as f:
                f.write('''
lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> mtu 16384
	options=3<RXCSUM,TXCSUM>
	inet6 ::1 prefixlen 128
	inet6 fe80::1%lo0 prefixlen 64 scopeid 0x1
	inet 127.0.0.1 netmask 0xff000000
gif0: flags=8010
