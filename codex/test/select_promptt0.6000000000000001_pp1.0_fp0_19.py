import select
# Test select.select

# select.select(rlist, wlist, xlist[, timeout])
#
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition”
# timeout: how long to wait
#
# If the timeout period expires without any of the conditions becoming true,
# all three lists are empty,
# and the function returns three empty lists.

import socket
import sys
import time

host = ''
port = 51423
backlog = 5
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(backlog)
input = [s] # input list
running = 1

while running:
    inputready, outputready, exceptready = select.select(input, [], [])

    for s in inputready:
        if s == s:
            client, address = s.accept()
            input.append(client)
            print('Accepted connection from', address)
