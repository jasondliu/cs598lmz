import select
# Test select.select with a large number of file descriptors.
# It used to crash with a ValueError because some of the internal
# fd_sets could not be allocated.

SOCKS = [socket.socket() for n in range(1024)]
for s in SOCKS:
    s.bind(('127.0.0.1', 0))
    s.listen(1)

rlist, wlist, xlist = select.select(SOCKS, SOCKS, SOCKS, 0)
for s in SOCKS:
    s.close()

#print 'rlist', map(lambda s:s.getsockname(), rlist)
#print 'wlist', map(lambda s:s.getsockname(), wlist)
#print 'xlist', map(lambda s:s.getsockname(), xlist)
