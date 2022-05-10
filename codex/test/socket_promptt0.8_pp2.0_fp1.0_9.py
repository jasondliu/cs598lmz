import socket
# Test socket.if_indextoname
print(socket.if_indextoname(1))
# Test socket.if_nameindex
print(socket.if_nameindex())
# Test socket.getaddrinfo
print(socket.getaddrinfo(
    '127.0.0.1',
    80,
    0,
    0,
    socket.SOL_TCP,
))
# Test socket.getnameinfo
print(socket.getnameinfo(('127.0.0.1', 80), 0))
# Test socket.getfqdn
print(socket.getfqdn())
# Test socket.gethostbyname
print(socket.gethostbyname('localhost'))
# Test socket.gethostbyname_ex
print(socket.gethostbyname_ex('localhost'))
# Test socket.gethostbyaddr
print(socket.gethostbyaddr('127.0.0.1'))
