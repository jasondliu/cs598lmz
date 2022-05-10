import socket
# Test socket.if_indextoname
print(socket.if_indextoname(1))

# Test socket.if_nameindex
print(socket.if_nameindex())

# Test socket.if_nametoindex
print(socket.if_nametoindex("lo"))

# Test socket.sockatmark
print(socket.socket().sockatmark())

# Test socket.socketpair
print(socket.socketpair())

# Test socket.gethostbyaddr
print(socket.gethostbyaddr("127.0.0.1"))

# Test socket.gethostbyname
print(socket.gethostbyname("localhost"))

# Test socket.gethostbyname_ex
print(socket.gethostbyname_ex("localhost"))

# Test socket.gethostname
print(socket.gethostname())

# Test socket.getprotobyname
print(socket.getprotobyname("tcp"))

# Test socket.getservbyname
print(socket.getservbyname("telnet"))

# Test socket.getservbyport
print(socket.getserv
