import socket
# Test socket.if_indextoname

import support

print socket.if_indextoname(1)

try:
    socket.if_indextoname(0)
except ValueError:
    pass
else:
    raise support.TestError('Should not have succeeded')

try:
    socket.if_indextoname(None)
except TypeError:
    pass
else:
    raise support.TestError('Should not have succeeded')
