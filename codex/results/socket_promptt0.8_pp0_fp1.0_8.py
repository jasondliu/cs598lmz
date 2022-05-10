import socket
# Test socket.if_indextoname()

print socket.if_indextoname(1)
print repr(socket.if_indextoname(2))
try:
    socket.if_indextoname(int(1e10))
except socket.error, msg:
    print msg
