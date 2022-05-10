import socket
# Test socket.if_indextoname

import socket
import sys

from test_support import verbose

if not hasattr(socket, 'if_indextoname'):
    raise ImportError("socket.if_indextoname not defined -- skipping test_if_indextoname")

if verbose:
    print 'socket.if_indextoname =', socket.if_indextoname

if sys.platform == 'darwin':
    # Darwin doesn't have a loopback interface
    lo_name = 'lo0'
else:
    lo_name = 'lo'

if verbose:
    print 'lo_name =', lo_name

lo_index = socket.if_nametoindex(lo_name)

if verbose:
    print 'lo_index =', lo_index

lo_name2 = socket.if_indextoname(lo_index)

if verbose:
    print 'lo_name2 =', lo_name2

if lo_name != lo_name2:
    raise RuntimeError("socket.if_indextoname(socket
