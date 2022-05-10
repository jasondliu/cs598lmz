import socket
# Test socket.if_indextoname()

ifname = "lo"

ifdev = socket.if_indextoname(socket.if_nametoindex(ifname))
print(ifdev)
