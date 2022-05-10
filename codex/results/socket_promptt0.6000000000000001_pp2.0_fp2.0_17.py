import socket
# Test socket.if_indextoname()
print(socket.if_indextoname(1))

# Test socket.if_nameindex()
print(socket.if_nameindex())

# Test socket.if_nametoindex()
print(socket.if_nametoindex('lo'))

# Test socket.getaddrinfo()
print(socket.getaddrinfo('www.python.org', 'http'))

# Test socket.getfqdn()
print(socket.getfqdn('www.python.org'))

# Test socket.gethostbyname_ex()
print(socket.gethostbyname_ex('www.python.org'))

# Test socket.gethostbyaddr()
print(socket.gethostbyaddr('8.8.8.8'))

# Test socket.gethostname()
print(socket.gethostname())

# Test socket.getnameinfo()
# print(socket.getnameinfo((2, 1), 0))

# Test socket.getprotobyname()
print(socket.getprotobyname('tcp'))


