import socket
# Test socket.if_indextoname():
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', 9999))
print(s.getsockname()[0])
print(socket.if_indextoname(s.getsockname()[0]))
print(socket.if_nameindex())
print(socket.if_nametoindex('eth0'))
print(socket.if_nameindex()[1][1])
print(socket.if_indextoname(socket.if_nameindex()[1][0]))

# Test gethostbyaddr():
print(socket.gethostbyaddr("127.0.0.1"))
print(socket.gethostbyaddr("192.168.1.1"))
print(socket.gethostbyaddr("8.8.8.8"))
#print(socket.gethostbyaddr("192.168.1.1"))
"""
"""
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', 9999))
