import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, block until a monitored file descriptor is ready; if specified as a float, it specifies a timeout in seconds; as a tuple, it specifies a timeout in seconds and microseconds

# Return value: three lists of objects that are ready: subsets of the first three arguments

# select.select() is a useful way to multiplex input from multiple sockets, but it’s not available on all platforms.

# The following example shows how to use select() to monitor two sockets at the same time, and exit as soon as one of them has data ready to be processed:

import socket
import select

s = socket.socket()

# get local machine name
host = socket.gethostname()

port = 9999

# bind to the port
s.bind((host, port))

#
