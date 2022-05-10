import socket
# Test socket.if_indextoname
print socket.if_indextoname(1)

# Test socket.if_nametoindex
print socket.if_nametoindex('lo')

# Test socket.getaddrinfo
print socket.getaddrinfo(socket.if_indextoname(1), 80, 0, 0, socket.SOL_TCP)

# Test socket.getnameinfo
print socket.getnameinfo(('127.0.0.1', 80), 0)
