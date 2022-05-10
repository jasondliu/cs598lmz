import select
# Test select.select()
# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, it will block until a file descriptor is ready.
# if specified as a float, it specifies the timeout as a number of seconds.
# if specified as None, it will block until a file descriptor is ready.
# if specified as an integer, it specifies a timeout in milliseconds.
# return value: three lists of objects that are ready
# rlist: objects ready for reading
# wlist: objects ready for writing
# xlist: objects with “exceptional conditions”

# Example:
# The following example shows how to use select to implement a timeout on accept:

import socket
import select

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 25000))
s.listen(1)

while True
