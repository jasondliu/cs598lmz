import socket
# Test socket.if_indextoname()
print(socket.if_indextoname(1))

# Test socket.if_nameindex()
print(socket.if_nameindex())

# Test socket.if_nametoindex()
print(socket.if_nametoindex('lo'))

# Test socket.socketpair()
# print(socket.socketpair())

# Test socket.getaddrinfo()
print(socket.getaddrinfo('www.python.org', 'http'))

# Test socket.gethostbyname()
print(socket.gethostbyname('www.python.org'))

# Test socket.gethostbyname_ex()
print(socket.gethostbyname_ex('www.python.org'))

# Test socket.gethostbyaddr()
print(socket.gethostbyaddr('216.58.209.206'))

# Test socket.gethostname()
print(socket.gethostname())

# Test socket.getnameinfo()
print(socket.getnameinfo(('216.58.209.206', 80), 0))

# Test socket
