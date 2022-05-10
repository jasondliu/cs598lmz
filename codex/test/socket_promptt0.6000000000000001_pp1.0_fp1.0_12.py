import socket
# Test socket.if_indextoname()
try:
    socket.if_indextoname(1)
except OSError:
    try:
        socket.if_indextoname(1)
    except OSError:
        pass
    else:
        raise Exception
else:
    raise Exception
# Test socket.if_nameindex()
try:
    socket.if_nameindex()
except OSError:
    try:
        socket.if_nameindex()
    except OSError:
        pass
    else:
        raise Exception
else:
    raise Exception
# Test socket.if_nametoindex()
try:
    socket.if_nametoindex('lo')
except OSError:
    try:
        socket.if_nametoindex('lo')
    except OSError:
        pass
    else:
        raise Exception
else:
    raise Exception
