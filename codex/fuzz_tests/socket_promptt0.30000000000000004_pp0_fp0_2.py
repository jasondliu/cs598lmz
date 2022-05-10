import socket
# Test socket.if_indextoname
try:
    socket.if_indextoname(1)
except AttributeError:
    pass
else:
    raise Exception("socket.if_indextoname() should not exist")

# Test socket.if_nameindex
try:
    socket.if_nameindex()
except AttributeError:
    pass
else:
    raise Exception("socket.if_nameindex() should not exist")

# Test socket.if_nametoindex
try:
    socket.if_nametoindex("lo")
except AttributeError:
    pass
else:
    raise Exception("socket.if_nametoindex() should not exist")
