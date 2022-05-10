import socket
# Test socket.if_indextoname() using a valid interface index and invalid
# interface index.

import test.support

if socket.if_indextoname is None:
    import unittest
    raise unittest.SkipTest('if_indextoname() not supported')

import fcntl
import os
import socket
import subprocess
import sys
import time
import unittest
import tempfile
import errno

from test import support
from test.support import TESTFN, reap_children, HOST, TEST_IPV6
from test.support import import_module
ed = import_module('errno', deprecated=True)

SIOCGIFINDEX = 0x8933
SIOCGIFFLAGS = 0x8913

IFF_UP = 0x1
IFF_BROADCAST = 0x2
IFF_LOOPBACK = 0x8
IFF_POINTOPOINT = 0x10
IFF_RUNNING = 0x40
IFF_MULTICAST = 0x1000

IFF_ALLMULTI = 0x200
IFF_NOARP = 0x80
IFF
