import socket
# Test socket.if_indextoname()
try:
    socket.if_indextoname(1)
except AttributeError:
    print("SKIP")
    import sys
    sys.exit()

ifname = socket.if_indextoname(1)
index = socket.if_nametoindex(ifname)
print("index:", index)
print("name:", ifname)
