import socket
# Test socket.if_indextoname with IPv6 interface index
socket.if_indextoname(0x1)
# Test socket.if_nameindex with IPv6 interface name
socket.if_nameindex('lo')
# Test socket.gethostbyname_ex with IPv6 addresses
socket.gethostbyname_ex('localhost')
# Test socket.getaddrinfo with IPv6 addresses
socket.getaddrinfo('localhost', 0)
# Test socket.getnameinfo with IPv6 addresses
socket.getnameinfo(('127.0.0.1', 0), 0)
# Test socket.gethostbyaddr with IPv6 addresses
socket.gethostbyaddr('::1')
# Test socket.gethostbyname_ex with IPv6 addresses
socket.gethostbyname_ex('::1')
# Test socket.gethostbyname_ex with IPv6 addresses
socket.gethostbyname_ex('::1')
# Test socket.gethostbyname_ex with IPv6 addresses
socket.gethostbyname_ex('::1')
# Test socket.gethostbyname_ex with IPv6 addresses
socket.gethostbyname
