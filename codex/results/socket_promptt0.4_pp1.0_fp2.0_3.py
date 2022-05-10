import socket
# Test socket.if_indextoname()
#
# The test server should be started on the local machine, with the
# following command line:
#
#     ./if_indextoname
#
# The test client can then be run in another window.
#
# The test server expects to be passed a single command line argument
# which is the port number on which to listen.

import sys
import socket
import select
import time
import struct

if sys.version_info[0] >= 3:
    from io import StringIO
else:
    from cStringIO import StringIO

def if_indextoname(ind):
    """Return the name of an interface given its index."""
    if not isinstance(ind, int):
        raise TypeError("an integer is required")
    if ind < 0:
        raise ValueError("if_indextoname() argument must be positive")
    try:
        return socket.if_indextoname(ind)
    except OSError as err:
        if err.errno != errno.ENXIO:
            raise
        return None

def get
