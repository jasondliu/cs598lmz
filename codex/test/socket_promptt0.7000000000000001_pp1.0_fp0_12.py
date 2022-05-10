import socket
# Test socket.if_indextoname()
# "lo" is always present on Linux, but may not be on other platforms.
# "lo" is the loopback device, so we know its index is 1
try:
    lo = socket.if_indextoname(1)
except OSError:
    print("socket.if_indextoname() not implemented")
else:
    print("socket.if_indextoname() returned %r" % lo)

# Test socket.if_nameindex()
names = socket.if_nameindex()
print("socket.if_nameindex() returned %d entries" % len(names))

# Test socket.if_nametoindex()
if lo:
    print("socket.if_nametoindex(%r) returns %d" % (lo, socket.if_nametoindex(lo)))
 
# Test socket.getaddrinfo()
socket.getaddrinfo('localhost', 80, socket.AF_INET, socket.SOCK_STREAM)

# Test socket.getnameinfo()
