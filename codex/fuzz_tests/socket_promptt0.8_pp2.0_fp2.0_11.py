import socket
# Test socket.if_indextoname
print(socket.if_indextoname(socket.if_nameindex()[0][0]))

# Test socket.if_nameindex
print(socket.if_nameindex())

# Test socket.if_nametoindex
print(socket.if_nametoindex('lo'))

# Test socket.ip_address
# Allowing the reading of the hostname
#print(socket.gethostbyname(socket.gethostname()))
#print(socket.gethostbyname_ex(socket.gethostname()))
#print(socket.gethostname())
#print(socket.gethostbyname_ex(socket.gethostname())[2])
print(socket.ip_address('lo'))
