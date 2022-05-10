import socket
# Test socket.if_indextoname()
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print(s.bind(('',0)))
print(s.getsockname())
print(socket.if_indextoname(s.getsockname()[1]))
s.close()

# Test socket.if_nameindex()
print(socket.if_nameindex())
