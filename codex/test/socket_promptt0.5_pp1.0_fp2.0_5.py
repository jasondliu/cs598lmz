import socket
# Test socket.if_indextoname
print(socket.if_indextoname(1))

# Test socket.gethostbyname_ex
print(socket.gethostbyname_ex('www.python.org'))

# Test socket.gethostbyaddr
print(socket.gethostbyaddr('216.58.221.100'))

# Test socket.getnameinfo
print(socket.getnameinfo(('216.58.221.100', 80, 0, 0), 0))

# Test socket.getaddrinfo
print(socket.getaddrinfo('www.python.org', 'http'))

# Test socket.getdefaulttimeout
print(socket.getdefaulttimeout())

# Test socket.create_connection
print(socket.create_connection(('www.python.org', 80)))

# Test socket.socketpair
print(socket.socketpair())

# Test socket.fromfd
print(socket.fromfd(0, socket.AF_INET, socket.SOCK_STREAM))

# Test socket.ntohs
print(socket.ntohs(0x1234))

