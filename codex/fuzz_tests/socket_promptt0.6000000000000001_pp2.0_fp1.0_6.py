import socket
# Test socket.if_indextoname
socket.if_indextoname(1)
# Socket module test
# Test socket.if_nameindex
socket.if_nameindex()
# Test socket.if_nametoindex
socket.if_nametoindex('lo')
# Test socket.getaddrinfo
socket.getaddrinfo('localhost', None)
# Test socket.gethostbyname
socket.gethostbyname('localhost')
# Test socket.gethostbyname_ex
socket.gethostbyname_ex('localhost')
# Test socket.gethostbyaddr
socket.gethostbyaddr('127.0.0.1')
# Test socket.gethostname
socket.gethostname()
# Test socket.getnameinfo
socket.getnameinfo(('127.0.0.1', 80), 0)
# Test socket.getprotobyname
socket.getprotobyname('tcp')
# Test socket.getservbyname
socket.getservbyname('http')
# Test socket.getservbyport
socket.getservbyport(80)
# Test socket.htons
socket.ht
