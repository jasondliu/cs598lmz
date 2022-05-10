import socket
# Test socket.if_indextoname(idx)

import test.test_support
from test.test_support import verbose, import_module, TESTFN, unlink
import random, time, errno
from ctypes import *
import sys



if test.test_support.is_android:
    # Android doesn't have socket.if_indextoname() at all, so we
    # cannot be sure it will work if we just skip the test.
    raise unittest.SkipTest("Android has no socket.if_indextoname()")

# We cannot be sure there is a socket module
socket = import_module('socket')

libc = CDLL(None)
libc.getifaddrs.restype = c_int
libc.getifaddrs.argtypes = [POINTER(POINTER(socket.ifaddrs))]
libc.freeifaddrs.restype = c_int
libc.freeifaddrs.argtypes = [POINTER(socket.ifaddrs)]

