import socket
# Test socket.if_indextoname()
try:
    socket.if_indextoname(1)
except socket.error as _:
    raise ImportError(
        "socket.if_indextoname() not available on this system")

import os
import sys
if '__pypy__' in sys.modules:
    # we are running on PyPy
    if sys.version_info < (3, 2):
        from select import poll, POLLIN
        from errno import EINTR
    elif sys.version_info < (3, 4):
        from select import poll, POLLIN, POLLNVAL
        from errno import EINTR
    else:
        from select import poll, POLLIN, POLLERR, POLLHUP
        from errno import EINTR, EAGAIN
else:
    # we are running on CPython
    if sys.version_info < (2, 6):
        from select import poll, POLLIN
        from errno import EINTR
    elif sys.version_info < (3, 1):
        from select import poll,
