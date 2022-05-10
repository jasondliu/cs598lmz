import socket
# Test socket.if_indextoname
try:
    socket.if_indextoname(1)
except AttributeError:
    pass
else:
    raise RuntimeError, 'ExpectedAttributeError'

# Test socket.if_nameindex
try:
    socket.if_nameindex()
except AttributeError:
    pass
else:
    raise RuntimeError, 'ExpectedAttributeError'

# Test socket.socketpair
try:
    socket.socketpair()
except AttributeError:
    pass
else:
    raise RuntimeError, 'ExpectedAttributeError'

# Test socket.fromfd
try:
    socket.fromfd(1, socket.AF_INET, socket.SOCK_DGRAM)
except AttributeError:
    pass
else:
    raise RuntimeError, 'ExpectedAttributeError'

# Test socket.ntohs
try:
    socket.ntohs(1)
except AttributeError:
    pass
else:
    raise RuntimeError, 'ExpectedAttributeError'

# Test socket.ntohl
try:
    socket.ntohl(1)

