import socket
# Test socket.if_indextoname()

import unittest
import os
import sys
import array
import struct
import fcntl
import errno
import socket

from test import test_support

def _ifname(ifindex):
    if not hasattr(socket, 'if_indextoname'):
        raise unittest.SkipTest('if_indextoname() not defined')
