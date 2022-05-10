import socket
# Test socket.if_indextoname()

import os
import sys

try:
    import fcntl
except ImportError:
    fcntl = None

# Linux only
if not sys.platform.startswith("linux"):
    sys.exit(0)

# If this test fails, you don't have a recent enough glibc.
if '2.7' not in sys.version:
    sys.exit(0)

# On Linux, socket.if_indextoname() returns the interface name
# corresponding to an interface index (a small integer).
#
# On Linux, socket.if_nametoindex() returns the interface index
# corresponding to an interface name.
#
# The interface name is a string.

if sys.version_info[:2] == (2, 6):
    # On Python 2.6, socket.if_indextoname() and socket.if_nametoindex()
    # are not available.  We use ctypes to call the glibc functions
    # if_nametoindex() and if_indextoname(), which are available on
   
