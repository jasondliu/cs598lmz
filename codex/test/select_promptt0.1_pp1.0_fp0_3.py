import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a monitored file descriptor becomes ready

# Return value: three lists of objects that are ready: subsets of the first three arguments

# select.select() is a useful way to multiplex input/output over a set of file descriptors.

# The following example shows how to use select() to monitor a pair of connected sockets.

# The first socket is used to accept incoming connections; the second is connected to a fixed peer address.
# Data is read from the incoming connections and echoed back.
# If there is no data to read, the program sleeps for one second.

# The program terminates when the fixed peer is closed.

import socket
import sys
import select

host = ''
port = 50000
backlog = 5
size = 1024
