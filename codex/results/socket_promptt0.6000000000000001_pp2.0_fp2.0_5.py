import socket
# Test socket.if_indextoname() and socket.if_nameindex()
from socket import AF_INET, AF_INET6, inet_pton, inet_ntop
try:
    socket.if_indextoname(0)
except (socket.error, AttributeError):
    print('SKIP')
    raise SystemExit

# Test IPv4 interface
name = socket.if_indextoname(1)
print(name)
addr = socket.if_nameindex()[1][1]
print(addr)
assert addr == socket.if_nametoindex(name)
assert addr == socket.if_nametoindex(name)

# Test IPv6 interface
name = socket.if_indextoname(2)
print(name)
addr = socket.if_nameindex()[2][1]
print(addr)
assert addr == socket.if_nametoindex(name)

# Test invalid interface
try:
    socket.if_indextoname(9999)
except OSError:
    print('OSError')

# Test invalid interface name
try:
   
