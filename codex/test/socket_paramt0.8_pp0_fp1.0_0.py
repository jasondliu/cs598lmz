import socket
socket.if_indextoname(3)

# get all interfaces at once
map(socket.if_indextoname, range(0,10))
