import socket
# Test socket.if_indextoname
print socket.if_indextoname(1)
# Test socket.getnameinfo
print socket.getnameinfo((socket.gethostname(), 80), 0)
