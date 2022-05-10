import select
# Test select.select

import socket
import select

s = socket.socket()
s.bind(('127.0.0.1', 0))
s.listen(1)

r, w, x = select.select([s], [], [], 1)

if s in r:
    print("socket is readable")
else:
    print("socket is not readable")

s.close()
