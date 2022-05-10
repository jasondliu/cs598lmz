import socket
# Test socket.if_indextoname()
print(socket.if_indextoname(5))
print(socket.if_indextoname(5))

# Test socket.if_nameindex()
print(socket.if_nameindex())

# Test socket.if_nametoindex()
print(socket.if_nametoindex("eth0"))

# Test socket.gethostname()
print(socket.gethostname())

# Get name info
print(socket.getnameinfo(("127.0.0.1", 80), 0))

# Get socket address
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 80))
print(s.getsockname())

# Get socket address
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 80))
print(s.getpeername())
