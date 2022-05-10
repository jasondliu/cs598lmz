import socket
# Test socket.if_indextoname function
import sys
from test_support import verbose, TestFailed

if verbose:
    print "Checking if_indextoname()"

ifname = socket.if_indextoname(1)
if verbose:
    print "interface name is ", ifname
if not sys.platform.startswith('linux'):
    raise TestFailed("if_indextoname() is only supported on linux")
if not ifname:
    raise TestFailed("if_indextoname returned invalid interface name")

try:
    socket.if_indextoname(-1)
except OSError, e:
    if e.errno != errno.EINVAL:
        raise TestFailed("if_indextoname should raise EINVAL, "
                         "got %r" % e)
else:
    raise TestFailed("if_indextoname should raise EINVAL")

try:
    socket.if_indextoname(1000000)
except OSError, e:
    if e.errno != errno
