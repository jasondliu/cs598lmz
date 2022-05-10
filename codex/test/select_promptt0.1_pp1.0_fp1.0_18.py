import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, block until a monitored file descriptor becomes ready

# Return value: three lists of objects that are ready: subsets of the first three arguments

# select.select() is a useful way to multiplex input from multiple sockets, and can be used to implement a simple web server.

# The following example shows how to use select() to multiplex input from two sockets and stdin.

# The example is a simple echo server that listens on port 5000 and echoes back whatever it receives.

# The server uses select() to handle two clients at a time.

# The server runs until killed with Ctrl-C.

import socket
import select

# Create a TCP/IP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
