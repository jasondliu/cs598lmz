import socket
# Test socket.if_indextoname
try:
    socket.if_indextoname(1)
except AttributeError:
    pass
else:
    raise RuntimeError("socket.if_indextoname should not be defined")

# Test socket.if_nameindex
try:
    socket.if_nameindex()
except AttributeError:
    pass
else:
    raise RuntimeError("socket.if_nameindex should not be defined")

# Test socket.if_nametoindex
try:
    socket.if_nametoindex("lo")
except AttributeError:
    pass
else:
    raise RuntimeError("socket.if_nametoindex should not be defined")

# Test socket.if_nameindex
try:
    socket.if_nameindex()
except AttributeError:
    pass
else:
    raise RuntimeError("socket.if_nameindex should not be defined")

# Test socket.if_freenameindex
try:
    socket.if_freenameindex(0)
except AttributeError:
    pass
