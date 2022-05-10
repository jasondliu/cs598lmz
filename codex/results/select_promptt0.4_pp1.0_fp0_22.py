import select
# Test select.select() with a socket that is not in blocking mode
# and a timeout of 0.

import select
import socket

s = socket.socket()
s.setblocking(False)
r, w, x = select.select([s], [s], [s], 0)
print r, w, x
