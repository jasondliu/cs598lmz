import socket
# Test socket.if_indextoname().  Not really a test.
if_nametoindex = socket.if_nametoindex(b"lo")
ifname = socket.if_indextoname(if_nametoindex)
assert ifname == b"lo"
print(ifname)

# TODO: Use unittest framework.
