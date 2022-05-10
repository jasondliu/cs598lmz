import socket
# Test socket.if_indextoname()
try:
    socket.if_indextoname(0)
except socket.error as e:
    pass
else:
    raise Exception("expected socket.error")
# Test socket.if_nameindex()
try:
    socket.if_nameindex()
except socket.error as e:
    pass
else:
    raise Exception("expected socket.error")

# Test socket.if_nameindex()
try:
    socket.sendfile()
except socket.error as e:
    pass
else:
    raise Exception("expected socket.error")

# Test socket.if_nameindex()
try:
    socket.recvfile()
except socket.error as e:
    pass
else:
    raise Exception("expected socket.error")
