import socket
# Test socket.if_indextoname function.

from test_support import verbose

prefix = 'lo'

if verbose:
    print 'testing socket.if_indextoname()'

for i in range(256):
    try:
        name = socket.if_indextoname(i)
    except socket.error, e:
        if e.args[0] != errno.ENXIO:
            raise
    else:
        if name.startswith(prefix):
            print i, name
            break
else:
    raise AssertionError, 'no lo interface found'
