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
if name != 'lo2':
    print 'socket.if_indextoname(2) did not return "lo2", received:', name
    sys.exit(1)


# Now test an invalid interface index.
interface_index = -1
try:
    name = if_indextoname(interface_index)

except IOError:
    exit_code = 0

else:
    print 'socket.if_indextoname() did not raise IOError'
    exit_code = 1

test_support.report('test_socket.test_if_indextoname()', exit_code)
