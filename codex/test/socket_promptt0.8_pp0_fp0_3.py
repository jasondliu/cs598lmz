import socket
# Test socket.if_indextoname
print(socket.if_indextoname(1))

# Test socket.if_nameindex()
print(socket.if_nametoindex('eth0'))

# Test socket.getaddrinfo()
print(socket.getaddrinfo('google.com', 80))

# Test socket.gethostbyname_ex()
print(socket.gethostbyname_ex('google.com'))

# Test socket.gethostbyaddr()
print(socket.gethostbyaddr('8.8.8.8'))

# Test socket.getfqdn()
print(socket.getfqdn('8.8.8.8'))

# Test socket.gethostname()
print(socket.gethostname())

# Test socket.getservbyname()
print(socket.getservbyname('http'))

# Test socket.getservbyport()
print(socket.getservbyport(80))

# Test socket.getprotobyname()
print(socket.getprotobyname('tcp'))

# Test socket.get
