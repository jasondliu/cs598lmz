import socket
# Test socket.if_indextoname
s = 'eth0'
print('Device name:', s)
print('Index', socket.if_indextoname(socket.if_nametoindex(s)))
