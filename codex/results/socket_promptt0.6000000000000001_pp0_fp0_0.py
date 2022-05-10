import socket
# Test socket.if_indextoname()
try:
    socket.if_indextoname(1)
except AttributeError:
    print('SKIP')
    raise SystemExit

# Test socket.if_indextoname()
print(socket.if_indextoname(1))

# Test socket.if_nameindex()
indexes = socket.if_nameindex()
print(indexes)

# Test socket.if_indextoname() on each index
for index in indexes:
    print(socket.if_indextoname(index[0]))
