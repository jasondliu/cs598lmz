import socket
# Test socket.if_indextoname()
print(socket.if_indextoname(1))

# Test socket.if_nameindex()
print(socket.if_nameindex())

# Test socket.if_nametoindex()
print(socket.if_nametoindex('lo'))

# Test socket.socketpair()
s1, s2 = socket.socketpair()
print(s1, s2)

# Test socket.getaddrinfo()
print(socket.getaddrinfo('www.google.com', 80))

# Test socket.getfqdn()
print(socket.getfqdn('127.0.0.1'))

# Test socket.gethostbyname()
print(socket.gethostbyname('www.google.com'))

# Test socket.gethostbyname_ex()
print(socket.gethostbyname_ex('www.google.com'))

# Test socket.gethostbyaddr()
print(socket.gethostbyaddr('127.0.0.1'))

# Test socket.gethostname()
print(socket.get
