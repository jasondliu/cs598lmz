import socket
socket.if_indextoname(3)

# if_nametoindex return the index of a given interface,
# or raise an exception if interface is not valid
socket.if_nametoindex('lo')
socket.if_nametoindex('eth0')
