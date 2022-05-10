import socket
# Test socket.if_indextoname
print("Interface index for eth0:", socket.if_indextoname(2))

# Test socket.if_nametoindex
print("Interface index for eth1:", socket.if_nametoindex("eth1"))
