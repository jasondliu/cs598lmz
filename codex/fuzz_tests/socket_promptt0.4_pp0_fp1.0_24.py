import socket
# Test socket.if_indextoname()

ifname = socket.if_indextoname(1)
print(ifname)

ifname = socket.if_indextoname(10)
print(ifname)

ifname = socket.if_indextoname(100)
print(ifname)

ifname = socket.if_indextoname(1000)
print(ifname)

ifname = socket.if_indextoname(10000)
print(ifname)
