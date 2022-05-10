import socket
# Test socket.if_indextoname
print(socket.if_indextoname(1))
print(socket.if_indextoname(4294967295))
try:
    socket.if_indextoname(4294967296)
except OSError as ex:
    print(ex)

# Test socket.if_nametoindex
print(socket.if_nametoindex('eth0'))
print(socket.if_nametoindex('eth4294967295'))

# Test socket.getifaddrs.ifaddr_hints, ifaddr_hints_get_ifclause_for_ifaddr
print(socket.getifaddrs())

# Test that ifaddr_hints.c_family is AF_UNSPEC by default.
print(socket.getifaddrs()[0].family == socket.AF_UNSPEC)

# Test that getifaddrs.addrs_hints is of type ifaddr_hints.
print(type(socket.getifaddrs()[0]))
# Test that getifaddrs.addrs_hints[0] is of
