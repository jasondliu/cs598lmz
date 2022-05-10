import socket
# Test socket.if_indextoname()
print(socket.if_indextoname(1))
try:
    print(socket.if_indextoname(65536))
except OSError as err:
    print('OS error: {0}'.format(err))

# Test socket.if_nameindex()
ifaces = socket.if_nameindex()
print('Active interfaces:')
for iface in ifaces:
    print(iface)

# Test socket.if_nametoindex()
try:
    print(socket.if_nametoindex('lo'))
except OSError as err:
    print('OS error: {0}'.format(err))

# Test socket.gethostbyname()
print(socket.gethostbyname('localhost'))

# Test socket.gethostbyname_ex()
print(socket.gethostbyname_ex('localhost'))

# Test socket.gethostname()
print(socket.gethostname())

# Test socket.gethostbyaddr()
