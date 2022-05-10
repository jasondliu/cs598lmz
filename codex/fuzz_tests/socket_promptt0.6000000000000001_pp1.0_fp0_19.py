import socket
# Test socket.if_indextoname(ifindex)

# We assume that we have at least one interface
ifindex = socket.if_nameindex()[0][0]
ifname = socket.if_indextoname(ifindex)
print(ifname)
