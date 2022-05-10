import socket
# Test socket.if_indextoname
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('192.168.1.1', 0))
print(sock.getsockname())
print(socket.if_indextoname(sock.fileno()))

# Test socket.if_nameindex
print(socket.if_nameindex())

# Test socket.if_nametoindex
print(socket.if_nametoindex('lo'))

# Test socket.getaddrinfo
print(socket.getaddrinfo('localhost', 8080))

# Test socket.getnameinfo
print(socket.getnameinfo(('127.0.0.1', 8080), 0))

# Test socket.gethostbyname
print(socket.gethostbyname('localhost'))

# Test socket.gethostbyname_ex
print(socket.gethostbyname_ex('localhost'))

# Test socket.gethostbyaddr
print(socket.gethostbyaddr('127.0.0.1'))

# Test socket.
