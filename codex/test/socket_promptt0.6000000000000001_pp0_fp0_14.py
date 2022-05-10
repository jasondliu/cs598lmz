import socket
# Test socket.if_indextoname()
print(socket.if_indextoname(2))

# Test socket.if_nameindex()
print(socket.if_nameindex())

# Test socket.if_nametoindex()
print(socket.if_nametoindex('lo'))

# Test socket.gethostbyname_ex()
print(socket.gethostbyname_ex('localhost'))

# Test socket.gethostbyaddr()
print(socket.gethostbyaddr('127.0.0.1'))

# Test socket.getnameinfo()
print(socket.getnameinfo(('127.0.0.1', 80), 0))

# Test socket.getaddrinfo()
print(socket.getaddrinfo('www.google.com', 'http'))

# Test socket.getaddrinfo()
print(socket.getaddrinfo('127.0.0.1', 80, 0, 0, socket.SOL_TCP))

# Test socket.getaddrinfo()
