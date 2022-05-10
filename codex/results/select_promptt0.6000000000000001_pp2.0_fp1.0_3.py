import select
# Test select.select
# select.select(rlist, wlist, xlist[, timeout])
# wait until one or more file descriptors are ready for some kind of I/O
# The first three arguments are sequences of file descriptors to be waited for
# timeout is an optional float specifying a timeout for the operation in seconds
# If the timeout argument is omitted the call blocks until at least one of the
# file descriptors is ready.
# A tuple of three lists is returned, corresponding to the first three arguments
# If the time limit is exceeded, three empty lists are returned

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
    inputready, outputready, exceptready = select.select(input, [], [])

   
