import socket
# Test socket.if_indextoname
print(socket.if_indextoname(1))
# Result: "lo"

import socket
# Test socket.if_nameindex
print(socket.if_nameindex())
# Result: [(1, 'lo')]

import socket
# Test socket.if_nametoindex
print(socket.if_nametoindex("lo"))
# Result: 1

import socket
# Test socket.getaddrinfo
print(socket.getaddrinfo("localhost", 8080))
# Result: [(<AddressFamily.AF_INET: 2>, <SocketKind.SOCK_STREAM: 1>, 6, '', ('127.0.0.1', 8080))]

import socket
# Test socket.gethostbyname
print(socket.gethostbyname("localhost"))
# Result: "127.0.0.1"

import socket
# Test socket.gethostbyname_ex
print(socket.gethostbyname_ex("localhost"))
# Result: ("localhost", [], ["127.0.0.1"])

import socket
# Test socket.getname
