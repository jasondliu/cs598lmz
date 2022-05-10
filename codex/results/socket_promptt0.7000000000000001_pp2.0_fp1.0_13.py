import socket
# Test socket.if_indextoname() on all possible interfaces
for i in range(0, 2**16):
    name = socket.if_indextoname(i)
    if name is not None:
        print(i, name)


#############################################
## Test socket.if_nameindex()
#############################################

import socket
# Test socket.if_nameindex()
interfaces = socket.if_nameindex()
for index, name in interfaces:
    print(index, name)


#############################################
## Test socket.if_nameindex() and socket.if_indextoname()
#############################################

import socket
interfaces = socket.if_nameindex()
for index, name in interfaces:
    print("%d %s" % (index, name))
    index2 = socket.if_nametoindex(name)
    print("%d %s" % (index2, socket.if_indextoname(index2)))
    print("")


#############################################
## Test socket.getaddrinfo()
#############################################

import socket
# Test socket.get
