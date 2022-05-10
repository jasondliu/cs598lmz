import socket
# Test socket.if_indextoname() to get the correct interface name.

import os, sys
import unittest
from test import test_support

# Skip test if AF_PACKET not defined
try:
    socket.AF_PACKET
except AttributeError:
    raise test_support.TestSkipped("socket module has no AF_PACKET constant")

if not hasattr(socket, 'if_indextoname'):
    raise test_support.TestSkipped("socket module has no if_indextoname() method")

class PacketSocketTests(unittest.TestCase):
    def testInterfaceName(self):
        # Get the interface name from /proc/net/dev
        # The format is
        # Inter-|   Receive                                                |  Transmit
        #  face |bytes    packets errs drop fifo frame compressed multicast|bytes    packets errs drop fifo colls carrier compressed
        #    lo: 6288670   60237    0    0    0     0          0         0  6288670   60237    0    0    0     0       0
