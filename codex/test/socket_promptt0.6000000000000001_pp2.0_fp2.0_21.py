import socket
# Test socket.if_indextoname()

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ifindex = s.getsockopt(socket.SOL_SOCKET, socket.SO_BINDTODEVICE, 4)
name = socket.if_indextoname(ifindex)
ifname = socket.if_nameindex()[1]
ifname = socket.if_nameindex(ifindex)
ifname = socket.if_nameindex(ifindex)[1]

# Test socket.if_nameindex()

ifname = socket.if_nameindex()
ifname = socket.if_nameindex()[1]

# Test socket.if_nameindex(ifindex)

ifname = socket.if_nameindex(ifindex)
ifname = socket.if_nameindex(ifindex)[1]
