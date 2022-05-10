import socket
# Test socket.if_indextoname()
print(socket.if_indextoname(1))

# Test socket.if_nameindex()
print(socket.if_nameindex())

# Test socket.if_nametoindex()
print(socket.if_nametoindex('lo'))

# Test socket.getaddrinfo()
print(socket.getaddrinfo('www.python.org', 'www', 0, 0, socket.SOL_TCP))

# Test socket.getnameinfo()
print(socket.getnameinfo(('127.0.0.1', 80), 0))

# Test socket.getfqdn()
print(socket.getfqdn('8.8.8.8'))

# Test socket.gethostbyname()
print(socket.gethostbyname('www.python.org'))

# Test socket.gethostbyname_ex()
print(socket.gethostbyname_ex('www.python.org'))

# Test socket.gethostbyaddr()
print(socket.gethostbyaddr('93.184.216.34'))

