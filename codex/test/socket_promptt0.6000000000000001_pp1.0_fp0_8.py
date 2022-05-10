import socket
# Test socket.if_indextoname

try:
    socket.if_indextoname
except AttributeError:
    print('AttributeError')
    raise SystemExit

try:
    socket.if_indextoname(1)
except OSError:
    pass  # No interface index 1 on this machine.
else:
    print('OSError not raised')

try:
    socket.if_indextoname(-1)
except OSError:
    pass  # No interface index -1 on this machine.
else:
    print('OSError not raised')

try:
    socket.if_indextoname(0)
except OSError:
    print('OSError raised')
else:
    print('OSError not raised')

try:
    socket.if_indextoname(0, 'foo')
except TypeError:
    print('TypeError raised')
else:
    print('TypeError not raised')

try:
    socket.if_indextoname(0, 0)
except TypeError:
    print('TypeError raised')
