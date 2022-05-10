import select
# Test select.select()
# wait until a socket is ready to be read/written
#
# select.select(rlist, wlist, xlist[, timeout])
#
# rlist: Check if these sockets are ready for reading
# wlist: Check if these sockets are ready for writing
# xlist: Check if these sockets have an error (exception)
# timeout: Timeout in seconds, or None for blocking

import socket

s = socket.socket()
s.bind(("localhost", 8888))
s.listen(5)

while True:
    rlist, wlist, xlist = select.select([s], [], [], 0)
    for sock in rlist:
        client, addr = sock.accept()
        print("Client connected from", addr)
