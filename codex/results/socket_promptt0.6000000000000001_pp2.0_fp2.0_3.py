import socket
# Test socket.if_indextoname
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print(socket.if_indextoname(s.getsockopt(socket.SOL_SOCKET, socket.SO_BINDTODEVICE, b'\xff'*4)))

# Test socket.if_nameindex
print(socket.if_nameindex())

# Test socket.if_nametoindex
print(socket.if_nametoindex("lo"))

# Test socket.getaddrinfo
print(socket.getaddrinfo("localhost", 0))

# Test socket.getnameinfo
print(socket.getnameinfo((socket.AF_INET, 8081), socket.NI_NUMERICSERV))

# Test socket.gethostbyname_ex
print(socket.gethostbyname_ex("localhost"))

# Test socket.gethostbyaddr
print(socket.gethostbyaddr("127.0.0.1"))
