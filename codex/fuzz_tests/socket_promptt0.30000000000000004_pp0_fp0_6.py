import socket
# Test socket.if_indextoname()

import os
import sys
import unittest
import subprocess
import errno
import socket
import platform
from test import support

import ifaddr

# Skip test if there is no interface
# Skip test if there is no interface
try:
    ifaddr.get_adapters()
except OSError as e:
    if e.errno == errno.ENOENT:
        raise unittest.SkipTest("no interface")

if sys.platform == 'win32':
    import _socket
    import ctypes
    import ctypes.wintypes
    from ctypes import windll

    def if_indextoname(index):
        """Return the name of the interface corresponding to the given index."""
        # This is a copy of the function in socketmodule.c, but with the
        # error handling removed.
        buf = ctypes.create_unicode_buffer(1024)
        if windll.iphlpapi.GetInterfaceNameForLanApiW(index, buf, 1024) == 0:
            return buf.value
        else:
           
