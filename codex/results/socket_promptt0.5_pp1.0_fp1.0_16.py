import socket
# Test socket.if_indextoname()
print(socket.if_indextoname(1))

# Test socket.if_nameindex()
print(socket.if_nameindex())

# Test socket.if_nametoindex()
print(socket.if_nametoindex('lo'))

# Test socket.getaddrinfo()
print(socket.getaddrinfo('www.google.com', 80, 0, 0, socket.IPPROTO_TCP))

# Test socket.gethostbyaddr()
print(socket.gethostbyaddr('8.8.8.8'))

# Test socket.gethostbyname()
print(socket.gethostbyname('www.google.com'))

# Test socket.gethostbyname_ex()
print(socket.gethostbyname_ex('www.google.com'))

# Test socket.gethostname()
print(socket.gethostname())

# Test socket.getnameinfo()
print(socket.getnameinfo(('www.google.com', 80), 0))

# Test socket.getprotobyname()
print
