import socket
# Test socket.if_indextoname

import socket

socket.if_indextoname(1)
socket.if_indextoname(socket.if_nametoindex('lo'))

try:
    socket.if_indextoname(0)
except ValueError:
    print("ValueError")

try:
    socket.if_indextoname(100)
except ValueError:
    print("ValueError")

try:
    socket.if_indextoname('100')
except TypeError:
    print("TypeError")

try:
    socket.if_indextoname(1.0)
except TypeError:
    print("TypeError")
