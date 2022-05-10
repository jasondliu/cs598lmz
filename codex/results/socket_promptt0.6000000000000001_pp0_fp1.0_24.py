import socket
# Test socket.if_indextoname()
if socket.if_indextoname(1):
    print("if_indextoname() supported")
else:
    print("if_indextoname() not supported")

# Test socket.if_nametoindex()
if socket.if_nametoindex('lo'):
    print("if_nametoindex() supported")
else:
    print("if_nametoindex() not supported")

# Test socket.if_nameindex()
if socket.if_nameindex()[0][0]:
    print("if_nameindex() supported")
else:
    print("if_nameindex() not supported")

# Test socket.socket.recvmsg()
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 0))
s.sendmsg(b'', (), ('127.0.0.1', s.getsockname()[1]))
try:
    s.recvmsg()
    print("socket.socket.recvmsg() supported")
except
