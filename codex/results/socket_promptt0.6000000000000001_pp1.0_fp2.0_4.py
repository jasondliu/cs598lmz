import socket
# Test socket.if_indextoname()

ifname = socket.if_indextoname(0)
print("Interface %d: %s" % (0, ifname))
