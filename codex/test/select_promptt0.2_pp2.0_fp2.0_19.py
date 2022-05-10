import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not given, block until at least one file descriptor is ready; if zero, return immediately even if no file descriptors are ready; if given, block for at most that many seconds

# Return value: three lists of objects that are ready

# select.select() is a useful way to multiplex input from multiple sockets.
# It is also a way to implement a timeout on blocking socket operations.
# select.select() can be interrupted by a signal (this is a limitation that cannot be easily worked around).

# select.select() can be used to implement a timeout on blocking socket operations.
# The following example uses select.select() to implement a timeout on a blocking socket operation.

# The following example uses select.select() to implement a timeout on a blocking socket operation.

import socket
import select
import sys


