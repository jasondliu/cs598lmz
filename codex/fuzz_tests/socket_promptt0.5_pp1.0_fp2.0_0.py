import socket
# Test socket.if_indextoname()

print(socket.if_indextoname(socket.if_nametoindex('lo')))
