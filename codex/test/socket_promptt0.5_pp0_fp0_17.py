import socket
# Test socket.if_indextoname()
try:
    socket.if_indextoname(2)
except AttributeError:
    pass
else:
    raise Exception("if_indextoname() exists")

# Test socket.if_nametoindex()
try:
    socket.if_nametoindex("lo")
except AttributeError:
    pass
else:
    raise Exception("if_nametoindex() exists")

# Test socket.getaddrinfo()
try:
    socket.getaddrinfo(None, 0, socket.AF_UNSPEC, socket.SOCK_STREAM, 0, socket.AI_PASSIVE)
except AttributeError:
    pass
else:
    raise Exception("getaddrinfo() exists")

# Test socket.getnameinfo()
try:
    socket.getnameinfo(("127.0.0.1", 80), 0)
except AttributeError:
    pass
else:
    raise Exception("getnameinfo() exists")

# Test socket.gethostbyname_ex()
