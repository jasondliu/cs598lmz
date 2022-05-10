import socket
# Test socket.if_indextoname()
import sys

from test import support

try:
    socket.if_indextoname(0)
except OSError:
    raise support.TestSkipped("if_indextoname() not implemented")

if sys.platform.startswith("linux"):
    # On Linux, if_indextoname() may raise a ValueError if the index is not
    # valid.
    try:
        socket.if_indextoname(-1)
    except ValueError:
        pass
    else:
        raise support.TestFailed("if_indextoname(-1) didn't raise an exception")
    try:
        socket.if_indextoname(256)
    except ValueError:
        pass
    else:
        raise support.TestFailed("if_indextoname(256) didn't raise an exception")
