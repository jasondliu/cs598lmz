import socket
# Test socket.if_indextoname
print(socket.if_indextoname(1))

# Test socket.if_nameindex
print(socket.if_nameindex())

# Test socket.if_nameindex
print(socket.if_nameindex())

# Test socket.gethostbyaddr
print(socket.gethostbyaddr("8.8.8.8"))

# Test socket.gethostbyname
print(socket.gethostbyname("localhost"))

# Test socket.gethostbyname_ex
print(socket.gethostbyname_ex("localhost"))

# Test socket.getnameinfo
print(socket.getnameinfo(("127.0.0.1", 80), 0))

# Test socket.getnameinfo
print(socket.getnameinfo(("localhost", 80), 0))

# Test socket.getnameinfo
print(socket.getnameinfo(("localhost", 80), 0))

# Test socket.getnameinfo
print(socket.getnameinfo(("127.0.0.1", 80), 0))

# Test socket.getfqdn
print(
