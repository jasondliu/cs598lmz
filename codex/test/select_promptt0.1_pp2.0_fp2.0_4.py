import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not given, block until at least one file descriptor is ready; if zero, return three empty lists; if given, block until at least one file descriptor is ready or the timeout has elapsed, in which case the three lists will be empty.

# Return value: three lists of objects that are ready: subsets of the first three arguments.

# select.select() is a useful way to multiplex input from multiple sockets.

# Example:

import socket
import select

s = socket.socket()

# get local machine name
host = socket.gethostname()

port = 9999

# bind to the port
s.bind((host, port))

# queue up to 5 requests
s.listen(5)

inputs = [s]

while True:
    rs,
