import socket
# Test socket.if_indextoname() for a non-existing interface index.
import sys
import test_support

try:
    if_indextoname = socket.if_indextoname
except AttributeError:
    sys.exit(0) # Skip the test if this platform does not support
                # the requested interface.

interface_index = 2
name = if_indextoname(interface_index)
