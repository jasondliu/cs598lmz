import socket
# Test socket.if_indextoname()
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print(socket.if_indextoname(s.fileno(), 1))
"""
# Test socket.if_nameindex()
print(socket.if_nameindex())
# Test socket.if_nametoindex()
print(socket.if_nametoindex('lo'))
"""

# Test socket.sendto
#msg = b'test'
#s.sendto(msg, (socket.gethostname(), 1234))

print(socket.gethostbyaddr('192.168.122.1'))
print(socket.gethostbyname('localhost'))
# print(socket.gethostbyname_ex('localhost'))

# Test socket.gethostname()
print(socket.gethostname())

print(socket.gethostbyname_ex('localhost'))

print(socket.getfqdn('localhost'))
print(socket.getfqdn(socket.gethostname()))

print(socket.getprotobyname('ip
