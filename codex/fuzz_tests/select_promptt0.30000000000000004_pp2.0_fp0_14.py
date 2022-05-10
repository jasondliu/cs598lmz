import select
# Test select.select()

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 0))
s.listen(1)

print 'listening on', s.getsockname()

r, w, x = select.select([s], [], [], 2)
print 'r', r
print 'w', w
print 'x', x

r, w, x = select.select([s], [], [], 2)
print 'r', r
print 'w', w
print 'x', x

r, w, x = select.select([s], [], [], 2)
print 'r', r
print 'w', w
print 'x', x

r, w, x = select.select([s], [], [], 2)
print 'r', r
print 'w', w
print 'x', x

r, w, x = select.select([s], [], [], 2)
print 'r', r
print 'w', w
print 'x', x

r, w,
