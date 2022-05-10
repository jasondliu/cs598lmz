import socket
# Test socket.if_indextoname
# This function is not available on Windows (CPython 3.4)
try:
    socket.if_indextoname(1)
except AttributeError:
    pass

# Test socket.if_nametoindex
# This function is not available on Windows (CPython 3.4)
try:
    socket.if_nametoindex('lo')
except AttributeError:
    pass
