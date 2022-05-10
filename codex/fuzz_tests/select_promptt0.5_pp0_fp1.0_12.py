import select
# Test select.select()

# Select on a socket with data available

import select, socket

s = socket.socket()
s.setblocking(0)
s.bind(('', 0))
s.listen(5)

r, w, e = select.select([s], [], [], 0)
if s in r:
    print 'socket is readable'
else:
    print 'socket is not readable'

# Select on a socket with data available, but with a timeout

import select, socket

s = socket.socket()
s.setblocking(0)
s.bind(('', 0))
s.listen(5)

r, w, e = select.select([s], [], [], 1.0)
if s in r:
    print 'socket is readable'
else:
    print 'socket is not readable'

# Select on a socket with no data available

import select, socket

s = socket.socket()
s.setblocking(0)
s.bind(('', 0))
s.listen(5)

r, w, e
