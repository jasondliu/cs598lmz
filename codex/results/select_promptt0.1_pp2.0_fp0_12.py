import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not given, block until at least one file descriptor is ready; if zero, return three empty lists; if given, block for at least that long, or until at least one file descriptor is ready

# Return value: three lists of objects that are ready: subsets of the first three arguments

# select.select() is a useful way to multiplex input from multiple sockets, and can be used to implement a simple web server.

# Example:

import socket
import select

s = socket.socket()

# get local machine name
host = socket.gethostname()

port = 12345

# bind to the port
s.bind((host, port))

# queue up to 5 requests
s.listen(5)

inputs = [s]

while True:
    rs
