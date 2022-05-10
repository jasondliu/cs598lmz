import select
# Test select.select()
# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not given, block until at least one file descriptor is ready; else a float giving a timeout in seconds, or None

# Returns three lists of file descriptors: subsets of the first three arguments

import socket
import sys
import select

host = ''
port = 51423

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((host, port))
print('Listening at', server.getsockname())
server.listen(1)

while True:
    print('Waiting for a new connection')
    try:
        connection, client_address = server.accept()
    except KeyboardInterrupt:
