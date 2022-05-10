import socket
# Test socket.if_indextoname
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print(socket.if_indextoname(0))
try:
    print(socket.if_indextoname(0xff))
except socket.error as inst:
    print(str(inst))

# Test socket.if_nameindex
print(socket.if_nameindex())

# Test socket.if_nametoindex
print(socket.if_nametoindex('lo'))
print(socket.if_nametoindex('eth0'))
try:
    print(socket.if_nametoindex('xyz'))
except socket.error as inst:
    print(str(inst))

# Test socket.getnameinfo
print(socket.getnameinfo(('localhost', 0), 0))
print(socket.getnameinfo(('localhost', 0), socket.NI_NUMERICHOST))
print(socket.getnameinfo(('localhost', 0), socket.NI_NAMEREQD))
