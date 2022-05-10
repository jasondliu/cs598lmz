import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a monitored file descriptor becomes ready

# Return value: three lists of objects that are ready: subsets of the first three arguments

# select.select() is a useful way to multiplex input/output over a set of file descriptors.
# It can be used to implement a simple network server.

# The following example shows how to use select() to handle three inputs at once: stdin, a socket, and a file.

# The example is a simple echo server that listens on port 50007 and echoes back everything that is sent to it.
# It only handles one connection at a time, but it is able to handle input from the connection and from standard input at the same time.

import socket
import sys
import select

host = ''
port = 50007
backlog = 5
