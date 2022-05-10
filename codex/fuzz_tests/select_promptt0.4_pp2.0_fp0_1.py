import select
# Test select.select() with a timeout of 0.

import select
import socket
import time

# A timeout of 0 means that select() will return immediately, even if no
# file descriptors are ready.

# Create a pair of connected sockets
lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.bind(('localhost', 0))
lsock.listen(1)
addr, port = lsock.getsockname()
csock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
csock.connect((addr, port))
ssock, addr = lsock.accept()

# Set the sockets to non-blocking mode
csock.setblocking(0)
ssock.setblocking(0)

# Try a select() call with a timeout of 0.  It should return immediately
# with empty lists.
start = time.time()
r, w, e = select.select([csock], [csock], [], 0)
end = time.time()
assert (r, w, e) == ([], [],
