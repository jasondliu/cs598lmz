import socket
# Test socket.if_indextoname()

# If this test fails, it means the machine has no network interfaces
# at all.  If it succeeds, it means the machine has at least one
# interface, but it doesn't mean that any particular interface exists.

# XXX We should find a way to test whether a particular interface exists.

ifname = socket.if_indextoname(1)
print(ifname)
