import socket
# Test socket.if_indextoname()
try:
    socket.if_indextoname(1)
    raise Exception('socket.if_indextoname() does not require root privileges.')
except OSError as err:
    if err.errno != errno.EPERM:
        raise Exception('Unexpected exception when calling socket.if_indextoname()')
except Exception as err:
    raise Exception('Unexpected exception when calling socket.if_indextoname()')
# Test socket.if_nameindex()
try:
    socket.if_nameindex()
    raise Exception('socket.if_nameindex() does not require root privileges.')
except OSError as err:
    if err.errno != errno.EPERM:
        raise Exception('Unexpected exception when calling socket.if_nameindex()')
except Exception as err:
    raise Exception('Unexpected exception when calling socket.if_nameindex()')
# Test socket.if_nametoindex()
try:
    socket.if_nametoindex('lo')
    raise Exception('socket.if_nametoindex() does
