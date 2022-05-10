import socket
# Test socket.if_indextoname
print(socket.if_indextoname(2))

# Test socket.if_indextoname with invalid if_index
try:
    socket.if_indextoname(10)
except OSError as e:
    print(e.errno)

# Test socket.if_nameindex
print(socket.if_nameindex())
