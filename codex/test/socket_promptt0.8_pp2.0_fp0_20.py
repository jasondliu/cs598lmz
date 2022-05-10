import socket
# Test socket.if_indextoname()
try:
    socket.if_indextoname(1)
except socket.error as err:
    print('if_indextoname():', err)
else:
    print('if_indextoname():', socket.if_indextoname(1))

# Test socket.if_nametoindex()
try:
    socket.if_nametoindex('lo')
except socket.error as err:
    print('if_nametoindex():', err)
else:
    print('if_nametoindex():', socket.if_nametoindex('lo'))
