import socket
# Test socket.if_indextoname()
print socket.if_indextoname(1)
print socket.if_indextoname(2)

# Test socket.if_nameindex()
print socket.if_nameindex()
print socket.if_nameindex()[0]
print socket.if_nameindex()[1]

# Test socket.if_nametoindex()
print socket.if_nametoindex('lo')
print socket.if_nametoindex('eth0')

# Test socket.getnameinfo()
print socket.getnameinfo(('127.0.0.1', 80), 0)
print socket.getnameinfo(('127.0.0.1', 80), socket.NI_NUMERICHOST)
print socket.getnameinfo(('127.0.0.1', 80), socket.NI_NUMERICSERV)
print socket.getnameinfo(('127.0.0.1', 80), socket.NI_NOFQDN)
print socket.getnameinfo(('127.0.0.1', 80), socket.NI_NAMEREQD)
print
