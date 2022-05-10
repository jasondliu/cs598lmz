import select
# Test select.select() with all FDs closed.
import socket
import sys
import time

# Create a bunch of sockets.  Some of them will be closed.
socks = []
for i in range(100):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setblocking(0)
    try:
        sock.bind(('', 0))
        sock.listen(1)
    except socket.error:
        # Couldn't bind the socket.  Close it and ignore.
        sock.close()
    else:
        socks.append(sock)

# Close half of the sockets.
for i in range(len(socks) // 2):
    socks[i].close()

# Check that select works with all the sockets.
r, w, x = select.select(socks, [], [], 0)

# Check that the closed sockets are ignored.
if len(r) != len(socks) // 2:
    raise RuntimeError("select() returned %d sockets, expected %d" %
                       (len(
