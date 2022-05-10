import select
# Test select.select()

import socket

s = socket.socket()
s.bind(('', 0))
s.listen(5)

print("Listening on port %d" % s.getsockname()[1])

r, w, e = select.select([s], [], [], 1)
print("r = %r" % r)
print("w = %r" % w)
print("e = %r" % e)

r, w, e = select.select([s], [], [], 1)
print("r = %r" % r)
print("w = %r" % w)
print("e = %r" % e)

c, a = s.accept()
print("Connection from %s" % repr(a))

r, w, e = select.select([s], [], [], 1)
print("r = %r" % r)
print("w = %r" % w)
print("e = %r" % e)

r, w, e = select.select([s], [], [], 1)
print
