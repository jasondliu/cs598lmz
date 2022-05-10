import socket
# Test socket.if_indextoname on (maybe) non-existing interface
try:
    socket.if_indextoname(0)
except (socket.error, OSError) as e:
    if not e.args[0] in (errno.EPERM, errno.ENODEV):
        raise
else:
    raise Exception('non-existing interface did not raise socket error')

# Test socket.if_indextoname on existing interfaces
for i in range(0, 128):
    try:
        socket.if_indextoname(i)
        raise Exception('existing interface did not raise socket error')
    except (socket.error, OSError) as e:
        if not e.args[0] in (errno.EPERM,
            errno.ENONET, errno.EINVAL):
            raise

# Test socket.if_nameindex
