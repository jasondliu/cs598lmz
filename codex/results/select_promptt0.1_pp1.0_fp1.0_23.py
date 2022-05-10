import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not given, block until at least one file descriptor is ready; if zero, return three empty lists; if given, block until at least one file descriptor is ready or the timeout has elapsed, in which case the three lists will be empty

# Return value: three lists of objects that are ready: subsets of the first three arguments

# select.select() is a useful way to multiplex input from multiple sockets, and can be used to wait for data on many sockets at the same time.

# The following example shows how to use select() to monitor two sockets at the same time, and exit as soon as one of them receives some data (while the other socket remains monitored).

#!/usr/bin/env python

import socket
import select

# create a socket
s = socket.socket(socket.AF_INET,
