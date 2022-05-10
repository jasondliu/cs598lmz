import socket
# Test socket.if_indextoname()
print(socket.if_indextoname(1))
# Test socket.if_nameindex()
print(socket.if_nameindex())
# Test socket.if_nametoindex()
print(socket.if_nametoindex('lo'))

# Test socket.getaddrinfo()
print(socket.getaddrinfo('www.python.org', 'http'))
print(socket.getaddrinfo('www.python.org', 'http', 0, socket.SOCK_STREAM, 0, socket.AI_PASSIVE))

# Test socket.gethostbyaddr()
print(socket.gethostbyaddr('192.168.1.2'))

# Test socket.gethostbyname()
print(socket.gethostbyname('www.python.org'))

# Test socket.gethostbyname_ex()
print(socket.gethostbyname_ex('www.python.org'))

# Test socket.gethostname()
print(socket.gethostname())

# Test socket.getnameinfo()
print(socket.getnameinfo(('
