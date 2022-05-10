import socket
# Test socket.if_indextoname()
import array
import ctypes
import struct
import os
import platform
import sys
import time
import unittest
import weakref
import errno
import selectors

from test import support
from test.support import import_module

import_module('ctypes')

import_module('ctypes.wintypes')

import_module('multiprocessing')

HAVE_PROC_PID_STATUS = False
try:
    f = open('/proc/%d/status' % os.getpid())
except IOError:
    pass
else:
    HAVE_PROC_PID_STATUS = True
    f.close()

#
# Tests to check the state of the current process
#

#
# Use ctypes to determine the current number of open file descriptors
#
if sys.platform.startswith('linux'):
    import ctypes

    # Some constants from bits/fcntl.h
    F_GETFD = 1
    FD_CLOEXEC = 1

