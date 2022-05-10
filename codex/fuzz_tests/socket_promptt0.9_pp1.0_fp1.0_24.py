import socket
# Test socket.if_indextoname()
print(socket.if_indextoname(2))
# Print all sockets on your system (index, name, ip address)
for inx in socket.if_nameindex():
    print(inx)
    print(socket.if_indextoname(inx[0]))

# Test socket.if_nametoindex()
print(socket.if_nametoindex('lo'))

# Test socket.gethostname()
print(socket.gethostname())
print(socket.getfqdn(socket.gethostname()))
