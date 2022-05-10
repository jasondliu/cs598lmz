import socket
# Test socket.if_indextoname()

from test_support import verbose, TestFailed

if_indextoname = socket.if_indextoname

if verbose:
    print '\nTesting socket.if_indextoname()'

if_indextoname(1)

try:
    if_indextoname(0)
except socket.error:
    pass
else:
    raise TestFailed, 'expected socket.error'

try:
    if_indextoname(-1)
except socket.error:
    pass
else:
    raise TestFailed, 'expected socket.error'
