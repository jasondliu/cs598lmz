import socket
# Test socket.if_indextoname()
print('socket.if_indextoname({:d}): {}'.format(
    socket.if_indextoname(5),
    socket.if_indextoname(5)))
