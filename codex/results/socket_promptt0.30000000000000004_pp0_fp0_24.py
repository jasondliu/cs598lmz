import socket
# Test socket.if_indextoname()

# Test socket.if_indextoname() with invalid index
try:
    socket.if_indextoname(-1)
except socket.error as e:
    if e.errno != errno.EINVAL:
        raise

# Test socket.if_indextoname() with valid index
if socket.if_indextoname(1) != 'lo':
    raise Exception('socket.if_indextoname() failed')
