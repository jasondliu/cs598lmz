import socket
# Test socket.if_indextoname
print(socket.if_indextoname(1))
# Test socket.if_nameindex
print(socket.if_nameindex())
# Test socket.if_nametoindex
print(socket.if_nametoindex('lo'))
# Test socket.socketpair
# Test socket.getfqdn
print(socket.getfqdn())
# Test socket.gethostname
print(socket.gethostname())
# Test socket.gethostbyname
print(socket.gethostbyname('localhost'))
# Test socket.gethostbyname_ex
print(socket.gethostbyname_ex('localhost'))
# Test socket.gethostbyaddr
print(socket.gethostbyaddr('127.0.0.1'))
# Test socket.getaddrinfo
print(socket.getaddrinfo('localhost', 8080, 0, 0, socket.IPPROTO_TCP))
# Test socket.getnameinfo
print(socket.getnameinfo(('127.0.0.1', 8080), socket.NI_NUMERICSERV))
# Test socket.
