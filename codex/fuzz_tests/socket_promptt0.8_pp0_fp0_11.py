import socket
# Test socket.if_indextoname
print(socket.if_indextoname(1))
# Test socket.if_nameindex
print(socket.if_nameindex())
# Test socket.if_nametoindex
print(socket.if_nametoindex('wlp16s0'))
# Test socket.getaddrinfo
socket.getaddrinfo('google.com', 'https')
