import socket
# Test socket.if_indextoname
print(socket.if_indextoname(3))

# Test socket.if_nameindex
print(socket.if_nameindex())

# Test socket.if_nametoindex
print(socket.if_nametoindex('lo'))

# Test socket.getaddrinfo
print(socket.getaddrinfo("www.python.org", 80))

# Test socket.getdefaulttimeout
print(socket.getdefaulttimeout())

# Test socket.gethostbyaddr
print(socket.gethostbyaddr("127.0.0.1"))

# Test socket.gethostbyname
print(socket.gethostbyname("www.python.org"))

# Test socket.gethostbyname_ex
print(socket.gethostbyname_ex("www.python.org"))

# Test socket.gethostname
print(socket.gethostname())

# Test socket.gethostname (again)
print(socket.gethostname())

# Test socket.getnameinfo
print(socket.getnameinfo(('127.0.0.1', 0),
