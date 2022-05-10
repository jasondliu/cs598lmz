import socket
# Test socket.if_indextoname
try:
    socket.if_indextoname(0)
except AttributeError:
    pass
else:
    raise Exception("if_indextoname should raise AttributeError")

# Test socket.if_nameindex
try:
    socket.if_nameindex()
except AttributeError:
    pass
else:
    raise Exception("if_nameindex should raise AttributeError")

# Test socket.if_nametoindex
try:
    socket.if_nametoindex("lo")
except AttributeError:
    pass
else:
    raise Exception("if_nametoindex should raise AttributeError")

# Test socket.getaddrinfo
try:
    socket.getaddrinfo("www.python.org", 80, socket.AF_UNSPEC, socket.SOCK_STREAM)
except AttributeError:
    pass
else:
    raise Exception("getaddrinfo should raise AttributeError")

# Test socket.getnameinfo
try:
    socket.getnameinfo(("127.0.0.1", 80), socket.AF_UNSPEC,
