import socket
# Test socket.if_indextoname()

import unittest
import os
import sys
import errno
import array
import struct
import fcntl
import subprocess
from test import support

if not hasattr(socket, 'if_indextoname'):
    raise unittest.SkipTest("socket.if_indextoname not defined")

SIOCGIFNAME = 0x8910
SIOCGIFINDEX = 0x8933
SIOCGIFFLAGS = 0x8913
IFF_LOOPBACK = 0x8
IFF_UP = 0x1

class IfreqTest(unittest.TestCase):

    def setUp(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def tearDown(self):
        self.sock.close()

    def _get_ifname(self, ifindex):
        ifreq = struct.pack('I', ifindex)
        try:
            fcntl.ioctl(self.sock.fileno(), SIOCGIFNAME, ifreq
