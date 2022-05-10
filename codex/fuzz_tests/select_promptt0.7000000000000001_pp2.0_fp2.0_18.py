import select
# Test select.select()

# select.select(rlist, wlist, xlist, timeout=None)
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (not implemented on Windows)

# select.select() returns three lists of SOCKETs: subsets of the first three arguments.
# The first list contains those SOCKETs that are ready for reading, the second contains
# those that are ready for writing, and the third contains those that have triggered an
# “exceptional condition”.

# Example:
# The following code excepts a connection, sends a message, and terminates the connection.
# If no connection is pending, it waits up to five seconds and then returns to the caller.

import socket, sys
from time import ctime

host = ''
port = 51423

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s
