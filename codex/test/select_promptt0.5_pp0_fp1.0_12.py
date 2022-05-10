import select
# Test select.select()

# Select on a socket with data available

import select, socket

s = socket.socket()
s.setblocking(0)
s.bind(('', 0))
s.listen(5)

r, w, e = select.select([s], [], [], 0)
