import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a monitored file descriptor becomes ready

# Return value: three lists of objects that are ready: subsets of the first three arguments

# select.select() is a useful way to multiplex input and output, especially when there are multiple sockets to be monitored.

# Example:
# The following example shows how to use select() to monitor two sockets and stdin for input.

import sys
import socket
import select

host = ''
port = 50000
backlog = 5
size = 1024
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port))
server.listen(backlog)
input = [server,sys.stdin]
running = 1
while running:
    inputready,output
