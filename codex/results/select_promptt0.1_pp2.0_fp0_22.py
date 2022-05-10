import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)

# Return value: three lists of objects that are ready

# select.select() can be used as a way to wait until a file is ready for reading or writing.

# The following example waits for input on two sockets, or until a timer expires:

import socket
import sys
import select

host = ''
port = 51423

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((host, port))
server.listen(1)

input = [server, sys.stdin]

running = 1
while running:
    inputready, outputready, exceptready = select.select(input, [], [
