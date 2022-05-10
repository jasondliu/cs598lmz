import socket
# Test socket.if_indextoname
ifname = socket.if_indextoname(1)
# Test socket.if_nameindex
iflist = socket.if_nameindex()
# Test socket.socketpair
s1, s2 = socket.socketpair()
# Test socket.getaddrinfo
socket.getaddrinfo('127.0.0.1', 80)
# Test socket.getnameinfo
socket.getnameinfo(('127.0.0.1', 80), 0)
# Test socket.gethostbyname
socket.gethostbyname('localhost')
# Test socket.gethostname
socket.gethostname()
# Test socket.gethostbyaddr
socket.gethostbyaddr('127.0.0.1')
# Test socket.getservbyname
socket.getservbyname('http')
# Test socket.getservbyport
socket.getservbyport(80)
# Test socket.getprotobyname
socket.getprotobyname('tcp')
# Test socket.ntohs, socket.ntohl
socket.ntohs(10000)
socket.ntohl(10000
