import select
# Test select.select performance with a large number of file descriptors.

# See also: http://bugs.python.org/issue1026

# On Linux and OS X, this runs about 10x faster than Python 2.4.
# It is limited by the speed of poll() and select().

numfds = 1024
print 'creating %d sockets' % numfds
socks = [socket.socket() for i in range(numfds)]
print 'connecting %d sockets' % numfds
for s in socks:
    s.connect(('example.org', 80))

print 'selecting %d sockets' % numfds
# This is the slow part in Python 2.4
r, w, e = select.select(socks, socks, socks)

print 'closing %d sockets' % numfds
for s in socks:
    s.close()
