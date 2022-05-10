import select
# Test select.select() for asynchronous reader
#
# select.select(rlist, wlist, xlist[, timeout])
#
# Wait until one or more file descriptors are ready for some kind of I/O.
# The first three arguments are sequences of file descriptors to be waited
# for: rlist -- wait until ready for reading, wlist -- wait until ready
# for writing, xlist -- wait for an ``exceptional condition'' (see the
# manual page for what your system considers such a condition).

#print 'Time:', time.time()

#print 'Asynchronous read:'
#response = select.select([sock], [], [])
#print response

#rlist, wlist, xlist = select.select([time],[], [], 1)
#print rlist
#print wlist
#print xlist

#print 'Time:', time.time()

#sock.sendall('0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567
