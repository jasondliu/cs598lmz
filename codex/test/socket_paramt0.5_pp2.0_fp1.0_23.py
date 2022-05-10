import socket
socket.if_indextoname(3)

# Or
socket.if_indextoname(socket.if_nametoindex('eth0'))
