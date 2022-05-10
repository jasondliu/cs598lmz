import socket
# Test socket.if_indextoname()
print(socket.if_indextoname(1))

# Test socket.if_nameindex()
print(socket.if_nameindex())

# Test socket.if_nametoindex()
print(socket.if_nametoindex('lo'))

# Test socket.getaddrinfo()
print(socket.getaddrinfo('www.python.org', 'http'))

# Test socket.getaddrinfo()
print(socket.getaddrinfo('www.python.org', 'http', proto=socket.SOL_TCP))

# Test socket.getaddrinfo()
print(socket.getaddrinfo('www.python.org', 'http', proto=socket.SOL_TCP,
                         flags=socket.AI_CANONNAME))

# Test socket.getaddrinfo()
print(socket.getaddrinfo('www.python.org', 'http', proto=socket.SOL_TCP,
                         flags=socket.AI_CANONNAME, family=socket.AF_INET))

# Test socket.getaddrinfo()
print(socket.getaddr
