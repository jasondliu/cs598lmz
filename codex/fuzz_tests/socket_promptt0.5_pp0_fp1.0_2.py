import socket
# Test socket.if_indextoname()
try:
    socket.if_indextoname(1)
except socket.error:
    pass
else:
    raise TestFailed("if_indextoname() should have failed")

# Test socket.if_nameindex()
try:
    socket.if_nameindex()
except socket.error:
    pass
else:
    raise TestFailed("if_nameindex() should have failed")

# Test socket.if_nametoindex()
try:
    socket.if_nametoindex('')
except socket.error:
    pass
else:
    raise TestFailed("if_nametoindex() should have failed")

# Test socket.getnameinfo()
try:
    socket.getnameinfo(('127.0.0.1', 0), 0)
except socket.error:
    pass
else:
    raise TestFailed("getnameinfo() should have failed")

# Test socket.getaddrinfo()
try:
    socket.getaddrinfo(None, None)
except socket.error:
    pass
else:
    raise
