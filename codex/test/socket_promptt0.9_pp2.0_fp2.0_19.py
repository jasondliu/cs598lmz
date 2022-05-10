import socket
# Test socket.if_indextoname()
ifname = socket.if_indextoname(3)
print(ifname)

# Test socket.if_nameindex()
iflist = socket.if_nameindex()
