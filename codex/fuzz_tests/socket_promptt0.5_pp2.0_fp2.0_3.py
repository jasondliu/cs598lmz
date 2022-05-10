import socket
# Test socket.if_indextoname()
if_indextoname = socket.if_indextoname

# Test socket.if_nameindex()
if_nameindex = socket.if_nameindex

# Test socket.if_nametoindex()
if_nametoindex = socket.if_nametoindex

# Test socket.getaddrinfo()
try:
    socket.getaddrinfo(1, 1, 1, 1, 1)
except TypeError:
    pass
else:
    print("socket.getaddrinfo() doesn't raise TypeError")

# Test socket.gethostbyname()
try:
    socket.gethostbyname(1)
except TypeError:
    pass
else:
    print("socket.gethostbyname() doesn't raise TypeError")

# Test socket.gethostbyname_ex()
try:
    socket.gethostbyname_ex(1)
except TypeError:
    pass
else:
    print("socket.gethostbyname_ex() doesn't raise TypeError")

# Test socket.gethostname()
socket.gethostname()


