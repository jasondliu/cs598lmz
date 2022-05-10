import socket
# Test socket.if_indextoname
#
try:
    socket.if_indextoname(0)
except socket.error, e:
    if e.args[0] != errno.EINVAL:
        raise
else:
    raise RuntimeError('This platform does not support if_indextoname')
