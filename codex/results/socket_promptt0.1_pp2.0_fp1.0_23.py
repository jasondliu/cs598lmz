import socket
# Test socket.if_indextoname()

import unittest
import os
import sys
import errno
import array
import struct
import fcntl
import platform
import subprocess
import time

from test import support
from test.support import import_module

# Skip test if there is no if_indextoname()
try:
    socket.if_indextoname(1)
except AttributeError:
    raise unittest.SkipTest("if_indextoname not defined")

SIOCGIFNAME = 0x8910
SIOCGIFINDEX = 0x8933

def if_nametoindex(ifname):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        ifreq = struct.pack('16sH14s', ifname.encode('utf-8'), socket.AF_INET,
                            b'\0'*14)
        fcntl.ioctl(s.fileno(), SIOCGIFINDEX, ifreq)
        return struct.unpack('16sH14s',
