import socket
# Test socket.if_indextoname() with an invalid index:
try:
    socket.if_indextoname(0xffffffff)
except OSError as e:
    err = e.args[0]
    if err != errno.EINVAL:
        raise
# Test socket.if_indextoname() with an invalid length:
try:
    socket.if_indextoname(1, -1)
except ValueError:
    pass
else:
    raise Exception("socket.if_indextoname() failed to raise")
