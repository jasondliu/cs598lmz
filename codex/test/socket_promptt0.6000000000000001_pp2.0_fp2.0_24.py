import socket
# Test socket.if_indextoname() for valid index

import os, sys

if not hasattr(socket, 'if_indextoname'):
    raise SystemExit

for i in range(256):
    try:
        name = socket.if_indextoname(i)
    except OSError as msg:
        if msg.args[0] != errno.EINVAL:
            raise SystemExit('if_indextoname(%d): %r' % (i, msg))
    else:
        print('%2d %s' % (i, name))
