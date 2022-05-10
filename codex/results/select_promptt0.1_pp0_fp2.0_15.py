import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)

# Return value: three lists of objects that are ready

# select.select() can be used to wait for a socket to be ready for reading, writing or to have an out-of-band condition pending.

# The following example uses select() to wait for a socket to be readable, writable or to have an exceptional condition (or a combination of these).

import socket
import select

s = socket.socket()

# get the local machine name
host = socket.gethostname()

port = 1234

# bind to the port
s.bind((host, port))

# queue up to 5 requests
s.listen(5)

inputs = [s]

while True:
    rs, ws, es = select.select(inputs, [], [])
    for
