import socket
# Test socket.if_indextoname()

import os
import sys
import time
import struct
import select
import errno
import signal
import socket
import fcntl
import ifaddr

import unittest
import platform

if sys.version_info >= (3, 0):
    from io import StringIO
else:
    from StringIO import StringIO

# Skip test if there is no lo interface
try:
    socket.if_nametoindex('lo')
except OSError as e:
    if e.errno == errno.ENODEV:
        raise unittest.SkipTest("No lo interface")
    raise

# Skip test if the platform does not support the SIOCGIFADDR ioctl
if not hasattr(socket, 'SIOCGIFADDR'):
    raise unittest.SkipTest("platform does not support SIOCGIFADDR ioctl")

class IFAddrTests(unittest.TestCase):

    def setUp(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM
