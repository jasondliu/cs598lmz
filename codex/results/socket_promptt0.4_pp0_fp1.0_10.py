import socket
# Test socket.if_indextoname
print(socket.if_indextoname(1))
# Test socket.if_nameindex
print(socket.if_nameindex())
# Test socket.if_nametoindex
print(socket.if_nametoindex('lo'))
# Test socket.getaddrinfo
print(socket.getaddrinfo('www.python.org', 'http'))
# Test socket.gethostbyname_ex
print(socket.gethostbyname_ex('www.python.org'))
# Test socket.gethostbyaddr
print(socket.gethostbyaddr('127.0.0.1'))
# Test socket.getservbyname
print(socket.getservbyname('http'))
# Test socket.getservbyport
print(socket.getservbyport(80))
# Test socket.gethostname
print(socket.gethostname())
# Test socket.gethostbyname
print(socket.gethostbyname('localhost'))
# Test socket.getfqdn
print(socket.getfqdn('localhost'))
# Test socket.gethostbyname
