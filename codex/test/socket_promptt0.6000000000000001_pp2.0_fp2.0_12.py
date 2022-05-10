import socket
# Test socket.if_indextoname()
print(socket.if_indextoname(1))

# Test socket.if_nameindex()
print(socket.if_nameindex())

# Test socket.if_nametoindex()
print(socket.if_nametoindex('eth0'))

# Test socket.getservbyname()
print(socket.getservbyname('http', 'tcp'))

# Test socket.getservbyport()
print(socket.getservbyport(80, 'tcp'))

# Test socket.gethostbyname()
print(socket.gethostbyname('www.google.com'))

# Test socket.gethostbyname_ex()
print(socket.gethostbyname_ex('www.google.com'))

# Test socket.gethostbyaddr()
print(socket.gethostbyaddr('216.58.212.132'))

# Test socket.getnameinfo()
print(socket.getnameinfo(('216.58.212.132', 80), socket.NI_NAMEREQD))

# Test socket.
