import socket
# Test socket.if_indextoname()
print(socket.if_indextoname(1))

# Test socket.if_nameindex()
print(socket.if_nameindex())

# Test socket.if_nametoindex()
print(socket.if_nametoindex('eth0'))

# Test socket.getfqdn()
print(socket.getfqdn('8.8.8.8'))

# Test socket.gethostbyaddr()
print(socket.gethostbyaddr('8.8.8.8'))

# Test socket.gethostbyname()
print(socket.gethostbyname('google.com'))

# Test socket.gethostbyname_ex()
print(socket.gethostbyname_ex('google.com'))

# Test socket.gethostname()
print(socket.gethostname())

# Test socket.getnameinfo()
print(socket.getnameinfo(('8.8.8.8', 80), 0))

# Test socket.getprotobyname()
print(socket.getprotobyname('tcp
