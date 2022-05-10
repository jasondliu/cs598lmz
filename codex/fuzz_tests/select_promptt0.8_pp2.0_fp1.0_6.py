import select
# Test select.select() on a unix socket

import os, sys, errno

# Create a pair of connected sockets
if not hasattr(select, "SOCK_NONBLOCK"):
    raise ImportError("SOCK_NONBLOCK is not defined on this platform")
if not hasattr(select, "SOCK_CLOEXEC"):
    raise ImportError("SOCK_CLOEXEC is not defined on this platform")

# Test an unnamed socket
sv1, sv2 = socket.socketpair()

for s in [sv1, sv2]:
    try:
        fileno = s.fileno()
    except socket.error as e:
        if e.args[0] == errno.EBADF:
            # Python issue #4921
            print('SKIP')
            sys.exit()
        raise
    print(fileno, ':', s.getsockopt(socket.SOL_SOCKET, socket.SO_TYPE))
    # settimeout() required so that select() won't hang when given
    # non-blocking sockets.
    s.set
