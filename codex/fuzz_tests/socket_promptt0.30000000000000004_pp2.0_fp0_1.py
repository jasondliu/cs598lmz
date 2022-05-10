import socket
# Test socket.if_indextoname

# Test with invalid interface index
try:
    socket.if_indextoname(-1)
except ValueError:
    pass
else:
    raise Exception("socket.if_indextoname(-1) didn't raise ValueError")

# Test with valid interface index
if socket.if_indextoname(1) != 'lo':
    raise Exception("socket.if_indextoname(1) != 'lo'")
