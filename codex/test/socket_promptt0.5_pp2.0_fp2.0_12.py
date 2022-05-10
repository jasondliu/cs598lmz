import socket
# Test socket.if_indextoname()

import support
import sys
import os

if not hasattr(socket, "if_indextoname"):
    raise support.TestError("socket module has no if_indextoname()")

try:
    socket.if_indextoname(0)
except OSError as x:
    if x.args[0] == errno.EINVAL:
        raise support.TestError("if_indextoname() failed with EINVAL")
    else:
        raise support.TestError("if_indextoname() failed with %d" % x.args[0])

ifname = socket.if_indextoname(1)

if not ifname:
    raise support.TestError("if_indextoname() returned null")

if ifname == "lo":
    raise support.TestError("if_indextoname() returned 'lo' on non-loopback")

# Verify that if_indextoname() can be called with a string argument
