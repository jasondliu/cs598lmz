import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, block until a monitored file descriptor becomes ready

# Return value: three lists of objects that are ready

# select.select() is a useful way to multiplex input/output access to many file descriptors in a program.
# It can be used to implement a simple network server.

# The following example shows how to use select() to handle three inputs at once.

# The example is a simple echo server. It listens for connections on port 50007 and echoes whatever it receives back (though it does sleep for a second after each echo to simulate a long-running computation).
# The server runs until killed with Control-C.

import socket
import sys
import select

host = ''
port = 50007
backlog = 5
size = 1024
server = socket.socket(socket.AF_INET
