import select
# Test select.select

# select.select(rlist, wlist, xlist[, timeout])
#     rlist: wait until ready for reading
#     wlist: wait until ready for writing
#     xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
#     timeout: how long to wait, in seconds

# The return value is a tuple of three lists corresponding to the first three arguments; each contains the subset of the corresponding file objects that are ready

# The following example shows how to use select to monitor a pair of sockets and stdin for input at the same time:

import socket
import sys
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
    inputready,outputready,exceptready = select.select(input,[],[])

    for s in inputready
