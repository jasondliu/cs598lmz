import socket
# Test socket.if_indextoname
try:
    ifindex = socket.if_nametoindex('lo')
except (AttributeError, TypeError):
    raise NotImplementedError('socket.if_nametoindex or socket.if_indextoname')
socket.if_indextoname(ifindex)

# Test socket.getroute
addr = ('127.0.0.1', 50008)

socket.getaddrinfo(addr[0], addr[1])
socket.gethostbyname(addr[0])
socket.gethostbyname_ex(addr[0])
socket.gethostbyname_ex(addr[0]).pop()

try:
    socket.getroute(addr, addr)
except (AttributeError, TypeError):
    raise NotImplementedError('socket.getroute')
