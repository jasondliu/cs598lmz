import socket
# Test socket.if_indextoname()
interface_index = socket.if_nametoindex('lo')
print(interface_index)

print(socket.if_indextoname(interface_index))
