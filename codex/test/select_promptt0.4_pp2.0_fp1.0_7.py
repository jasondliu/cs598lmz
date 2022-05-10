import select
# Test select.select()
#
# Author: Lothar Rubusch, L.Rubusch@gmx.ch

import socket
import sys

# create a socket and bind it to a port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 8000))
s.listen(1)

# create a client socket
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(("localhost", 8000))

# test select.select()
while 1:
    (r, w, e) = select.select([s, c], [], [])
    if s in r:
        (clientsocket, address) = s.accept()
