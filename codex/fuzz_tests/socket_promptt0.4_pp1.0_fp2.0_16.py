import socket
# Test socket.if_indextoname
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print(socket.if_indextoname(s.getsockopt(socket.SOL_SOCKET, socket.SO_BINDTODEVICE)))

# Test socket.if_nameindex
print(socket.if_nameindex())

# Test socket.if_nametoindex
print(socket.if_nametoindex(socket.if_indextoname(s.getsockopt(socket.SOL_SOCKET, socket.SO_BINDTODEVICE))))

# Test socket.setdefaulttimeout
socket.setdefaulttimeout(10)
print(socket.getdefaulttimeout())

# Test socket.getaddrinfo
print(socket.getaddrinfo('www.python.org', 'http'))

# Test socket.getfqdn
print(socket.getfqdn('8.8.8.8'))

# Test socket.gethostbyaddr
print(socket.gethostbyaddr('8.8.8.8'))

# Test socket.
