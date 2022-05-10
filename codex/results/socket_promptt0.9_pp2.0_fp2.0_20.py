import socket
# Test socket.if_indextoname()
assert ('lo' == socket.if_indextoname(1))
# Test socket.if_nameindex()
if_nameindex = socket.if_nameindex()
for i in range(len(if_nameindex)):
    assert (i+1 == if_nameindex[i][0])
# Test socket.if_nametoindex()
assert (2 == socket.if_nametoindex('awlan0'))
# Test socket.socket()
sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
# Test socket.bind()
addr = socket.getaddrinfo('::1', 0, socket.AF_INET6, socket.SOCK_DGRAM, 0, socket.AI_PASSIVE)[0][4]
sock.bind(addr)
# Test socket.setsockopt()
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
