import select
# Test select.select()
# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)


# Example
# rlist is the input file descriptors to wait for read events on.
# wlist is the input file descriptors to wait for write events on.
# xlist is the input file descriptors to wait for an “exceptional condition” (eg. out-of-band data)
# timeout is the maximum time to wait for an event.
# timeout can be -1, 0 or >= 1. If it is -1, then the call returns only when an event happens on one of the file descriptors,
# if it is 0, then it returns if one of the file descriptors is ready,
# otherwise it returns in at most timeout seconds.

import socket
import select

# Create a TCP/IP socket
