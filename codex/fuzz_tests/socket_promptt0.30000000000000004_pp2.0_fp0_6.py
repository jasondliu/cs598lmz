import socket
# Test socket.if_indextoname()
print(socket.if_indextoname(1))

# Test socket.if_nametoindex()
print(socket.if_nametoindex('lo'))

# Test socket.gethostbyname()
print(socket.gethostbyname('localhost'))
print(socket.gethostbyname('127.0.0.1'))

# Test socket.gethostbyname_ex()
print(socket.gethostbyname_ex('localhost'))
print(socket.gethostbyname_ex('127.0.0.1'))

# Test socket.gethostname()
print(socket.gethostname())

# Test socket.gethostbyaddr()
print(socket.gethostbyaddr('127.0.0.1'))

# Test socket.getprotobyname()
print(socket.getprotobyname('tcp'))

# Test socket.getservbyname()
print(socket.getservbyname('http'))

# Test socket.getservbyport()
print(socket.getservbyport(80
