import socket
# Test socket.if_indextoname()
print(socket.if_indextoname(1))

# Test socket.gethostbyname_ex()
print(socket.gethostbyname_ex('www.baidu.com'))

# Test socket.gethostbyaddr()
print(socket.gethostbyaddr('119.75.217.109'))

# Test socket.getservbyname()
print(socket.getservbyname('http'))

# Test socket.getservbyport()
print(socket.getservbyport(80))

# Test socket.getprotobyname()
print(socket.getprotobyname('tcp'))

# Test socket.getprotobynumber()
print(socket.getprotobynumber(1))

# Test socket.getaddrinfo()
print(socket.getaddrinfo('www.baidu.com', 80))

# Test socket.getnameinfo()
print(socket.getnameinfo(('119.75.217.109', 80), 0))

# Test socket.getfqdn()
