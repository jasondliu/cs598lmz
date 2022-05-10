import socket
# Test socket.if_indextoname

# Test with invalid arguments
try:
    socket.if_indextoname()
except TypeError:
    pass
else:
    raise RuntimeError


try:
    socket.if_indextoname(1, 2, 3)
except TypeError:
    pass
else:
    raise RuntimeError

# Test with valid arguments
if socket.if_indextoname(1) != 'lo':
    raise RuntimeError
