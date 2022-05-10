import select
# Test select.select() with a large number of file descriptors.

import select
import socket
import sys
import time

# Create a bunch of sockets.
N = 100
sockets = []

for i in range(N):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('localhost', 0))
    s.listen(1)
    sockets.append(s)

# Wait for them to become readable.
r, w, x = select.select(sockets, [], [], None)
assert len(r) == N, "Expected %d sockets to be readable, got %d" % (N, len(r))

# Clean up.
for s in sockets:
    s.close()
