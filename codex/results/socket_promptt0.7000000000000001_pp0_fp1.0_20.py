import socket
# Test socket.if_indextoname
print(socket.if_indextoname(1))
print(socket.if_indextoname(2))
# Test socket.if_nameindex
print(socket.if_nameindex())

# Test socket.getaddrinfo()
print(socket.getaddrinfo(socket.gethostname(), None))
print(socket.getaddrinfo(socket.gethostname(), None, socket.AF_INET))
print(socket.getaddrinfo(socket.gethostname(), None, socket.AF_INET, socket.SOCK_STREAM))
print(socket.getaddrinfo(socket.gethostname(), None, socket.AF_INET, socket.SOCK_STREAM, 0))
print(socket.getaddrinfo(socket.gethostname(), None, socket.AF_INET, socket.SOCK_STREAM, 0, socket.AI_PASSIVE))

# Test socket.getnameinfo()
print(socket.getnameinfo(('127.0.0.1', 0), socket.NI_NAMEREQD))

# Test socket.gethostbyname
