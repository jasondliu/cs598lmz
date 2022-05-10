import socket
# Test socket.if_indextoname()
print(socket.if_indextoname(1))

# Test socket.if_nametoindex()
print(socket.if_nametoindex('lo'))

# Test socket.getaddrinfo()
print(socket.getaddrinfo('www.python.org', 'http'))

# Test socket.getnameinfo()
print(socket.getnameinfo(('127.0.0.1', 80), 0))

# Test socket.getservbyname()
print(socket.getservbyname('http', 'tcp'))

# Test socket.gethostbyname()
print(socket.gethostbyname('www.python.org'))

# Test socket.gethostbyaddr()
print(socket.gethostbyaddr('93.184.216.34'))

# Test socket.gethostname()
print(socket.gethostname())

# Test socket.gethostbyname_ex()
print(socket.gethostbyname_ex('www.python.org'))

# Test socket.getfqdn()
print(socket.
