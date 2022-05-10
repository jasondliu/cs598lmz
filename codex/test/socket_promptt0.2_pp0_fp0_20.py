import socket
# Test socket.if_indextoname()

# Test if_indextoname() with invalid index
try:
    socket.if_indextoname(-1)
except ValueError:
    pass
else:
    print('if_indextoname(-1) did not raise ValueError')

try:
    socket.if_indextoname(0)
except ValueError:
    pass
else:
    print('if_indextoname(0) did not raise ValueError')

try:
    socket.if_indextoname(1)
except ValueError:
    pass
else:
    print('if_indextoname(1) did not raise ValueError')

# Test if_indextoname() with valid index
if socket.if_indextoname(2) != 'lo':
    print('if_indextoname(2) returned %s' % socket.if_indextoname(2))
