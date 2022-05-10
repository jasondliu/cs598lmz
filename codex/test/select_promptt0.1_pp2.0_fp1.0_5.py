import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, block until a monitored file descriptor becomes ready

# Return value: three lists of objects that are ready: subsets of the first three arguments

# select.select() is a useful way to multiplex input from multiple sockets, and can be used to build multi-user servers.

# Example:
# The following example shows how to use select() to handle three sockets: stdin, s1, and s2.

# The example is a simple echo server that handles input from the user on stdin, and echoes it back to the user on s1 and s2.

# The example is written for simplicity, not efficiency.

# The example is written for simplicity, not efficiency.

import socket
import select
import sys

