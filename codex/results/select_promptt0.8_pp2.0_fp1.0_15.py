import select
# Test select.select: pass in a writable socket, it should return 
# immediately
print 'select.select(<socket>, [], [], 0)'
try:
    r, w, x = select.select(clientsocket, [], [], 0)
    print 'except expected'
except TypeError, e:
    print 'exception caught as expected: %s' % repr(e)
except Exception, e:
    print 'unexpected exception: %s' % repr(e)
else:
    print 'no exception - fail'


# Test that a non-blocking socket will timeout as expected:
print 'clientsocket.setblocking(0)'
clientsocket.setblocking(0)
print 'select.select([], [clientsocket], [], 0)'
try:
    r, w, x = select.select([], [clientsocket], [], 0)
    if r != [] and w != [clientsocket] and x != []:
        print 'select did not timeout as expected - fail'
except Exception, e:
    print 'unexpected exception: %s' % repr(e)
