import socket
# Test socket.if_indextoname
print(socket.if_indextoname(1))

# Test socket.if_nameindex
print(socket.if_nameindex())

# Test socket.if_nametoindex
print(socket.if_nametoindex('eth0'))

# Test socket.socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(s)
s.close()

# Test socket.socketpair
pair = socket.socketpair(socket.AF_INET, socket.SOCK_STREAM)
print(pair)
for s in pair:
    s.close()

# Test socket.getaddrinfo
print(socket.getaddrinfo("127.0.0.1", 8080, 0, 0, socket.IPPROTO_TCP))

# Test socket.gethostbyname
print(socket.gethostbyname("localhost"))

# Test socket.gethostbyname_ex
print(socket.gethostbyname_ex("localhost"))

# Test socket.gethostname
print(socket.gethostname())
