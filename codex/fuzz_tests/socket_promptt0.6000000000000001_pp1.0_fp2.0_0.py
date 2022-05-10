import socket
# Test socket.if_indextoname()
print(socket.if_indextoname(1))
# Test socket.if_nametoindex()
print(socket.if_nametoindex('lo'))

# Test socket.getnameinfo()
print(socket.getnameinfo(('127.0.0.1', 80), 0))
print(socket.getnameinfo(('127.0.0.1', 80), socket.NI_NUMERICHOST))
print(socket.getnameinfo(('127.0.0.1', 80), socket.NI_NUMERICSERV))
print(socket.getnameinfo(('127.0.0.1', 80), socket.NI_NOFQDN))
print(socket.getnameinfo(('127.0.0.1', 80), socket.NI_NAMEREQD))
print(socket.getnameinfo(('127.0.0.1', 80), socket.NI_DGRAM))

# Test socket.gethostbyaddr()
print(socket.gethostbyaddr('127.0.0.1'))

# Test socket.get
