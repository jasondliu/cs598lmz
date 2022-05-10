import select
# Test select.select() function
#
# select.select(rlist, wlist, xlist[, timeout])
#
# rlist -- list of file descriptors to be monitored for incoming data
# wlist -- list of file descriptors to be monitored for outgoing data
# xlist -- list of file descriptors to be monitored for exceptions
#
# timeout -- optional timeout value in seconds
#
# The return value is a triple of lists of objects that are ready:
# (rlist, wlist, xlist)

import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 10001))
s.listen(1)

inputs = [s]

while True:
    rs, ws, es = select.select(inputs, [], [])
    for r in rs:
        if r is s:
            client, address = s.accept()
            print("  connection from: ", address)
            inputs.append(client)
        else:
            data = r.recv(1024)
            if
