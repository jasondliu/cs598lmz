import socket
# Test socket.if_indextoname
print('if_indextoname({})'.format(socket.if_indextoname(0)))
print('if_indextoname({})'.format(socket.if_indextoname(1)))
# Test socket.if_nameindex
print('if_nameindex({})'.format(socket.if_nameindex()))
# Test socket.if_nametoindex
print('if_nametoindex({})'.format(socket.if_nametoindex('lo')))
