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
    try:
        return socket.if_indextoname(ifindex)
    except IOError, err:
        if err.errno != errno.EINVAL:
            raise
        raise unittest.SkipTest('if_indextoname() not supported')

def _ifindex(ifname):
    if not hasattr(socket, 'if_nametoindex'):
        raise unittest.SkipTest('if_nametoindex() not defined')
    try:
        return socket.if_nametoindex(ifname)
    except IOError, err:
        if err.errno != errno.EINVAL:
            raise
        raise unittest.SkipTest('if_
