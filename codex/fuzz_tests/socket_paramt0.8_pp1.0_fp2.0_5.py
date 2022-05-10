import socket
socket.if_indextoname(2)

It gives the name of interface 2. If the interface does not exist it raises ValueError.

"""
import socket, sys

a = socket.if_indextoname(2)
print(a)
