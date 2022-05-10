import socket
# Test socket.if_indextoname()

import socket
from test.test_support import verbose

if verbose:
    print "Test socket.if_indextoname() ..."

ifname = socket.if_indextoname(1)
if verbose:
    print "name of interface 1 is", ifname

# does it work with non existing interface?
try:
    ifname = socket.if_indextoname(10000)
except socket.error, msg:
    if verbose:
        print "socket.if_indextoname(10000) should have raised an exception"
    if msg[0] == socket.EINVAL:
        if verbose:
            print "exception EINVAL raised"
    else:
        raise
else:
    raise RuntimeError, "socket.if_indextoname(10000) should have raised EINVAL"
