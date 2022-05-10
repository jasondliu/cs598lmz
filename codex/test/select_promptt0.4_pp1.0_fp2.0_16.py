import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not supplied, block until a monitored file descriptor is ready; if supplied as a float with a nonzero value, it specifies a timeout in seconds; if supplied as None, block until a monitored file descriptor is ready

# Return value: three lists of objects that are ready: subsets of the first three arguments

# Example:

import sys
import socket
import select

host = ''
port = 51423

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((host, port))
server.listen(1)

inputs = [server]

