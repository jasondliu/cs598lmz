import socket
# Test socket.if_indextoname()

import os
import sys
import unittest
import socket

# Skip test if not Linux or no AF_PACKET
if not hasattr(socket, 'AF_PACKET'):
    raise unittest.SkipTest('AF_PACKET not defined')

if not hasattr(socket, 'if_indextoname'):
    raise unittest.SkipTest('if_indextoname not defined')

# Skip test if not root
if os.geteuid() != 0:
    raise unittest.SkipTest('not running as root')

class IfIndexToNameTest(unittest.TestCase):

    def test_if_indextoname(self):
        # Test socket.if_indextoname()
        self.assertEqual(socket.if_indextoname(1), 'lo')
        self.assertEqual(socket.if_indextoname(2), 'eth0')
        self.assertEqual(socket.if_indextoname(3), 'eth1')
