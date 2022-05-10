import socket
socket.if_indextoname(3)

#if_nameindex
socket.if_nameindex()

#if_nametoindex
socket.if_nametoindex('lo')

#inet_aton
socket.inet_aton('127.0.0.1')

#inet_ntoa
socket.inet_ntoa(b'\x7f\x00\x00\x01')

#inet_pton
socket.inet_pton(socket.AF_INET, '127.0.0.1')

#inet_ntop
socket.inet_ntop(socket.AF_INET, b'\x7f\x00\x00\x01')

#gethostbyname
socket.gethostbyname('localhost')

#gethostbyname_ex
socket.gethostbyname_ex('localhost')

#gethostbyaddr
socket.gethostbyaddr('127.0.0.1')

#getnameinfo
socket.getnameinfo(('127.0.0.1', 80), 0)

#getfqdn
socket.getfq
