import select
# Test select.select()

import socket

s = socket.socket()
s.bind(('', 0))
s.listen(1)

r, w, x = select.select([s], [], [], 1)
