import socket
# Test socket.if_indextoname()

import socket
import sys

if sys.platform == 'darwin':
    print('darwin: skipping test')
    sys.exit(0)

if_indextoname = socket.if_indextoname

if sys.platform.startswith('linux'):
    # On Linux, we can't assume that any particular interface is present,
    # so we just check that an OSError is raised for an invalid index.
    socket.if_indextoname(0)
else:
    # On other platforms, we can assume that at least lo0 is present.
    assert if_indextoname(0) == 'lo0'
    assert if_indextoname(1) == 'lo0'

try:
    if_indextoname(2)
except OSError as e:
    assert e.errno == errno.EINVAL
else:
    assert False, 'OSError not raised'
