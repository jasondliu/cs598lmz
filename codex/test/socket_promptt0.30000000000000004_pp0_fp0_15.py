import socket
# Test socket.if_indextoname()

# Test with invalid index
try:
    socket.if_indextoname(0)
except socket.error as e:
    print(e)

# Test with valid index
print(socket.if_indextoname(1))
