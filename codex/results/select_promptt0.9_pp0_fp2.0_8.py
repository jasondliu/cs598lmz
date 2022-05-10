import select
# Test select.select function which should always return immediately.
print select.select([], [], [])
# Issue #1300: infinite recursion when the parameters are bad.
try:
    select.select([4], [4], [4], 0)
except TypeError:
    pass
else:
    print 'TypeError not raised'

# Test select.poll object.

import select

print "creating poll object"
p = select.poll()
try:
    # Try to register and unregister a fd.
    p.register(1, 1)
except select.error, e:
    if e[0] != errno.ENOSYS:
        raise
else:
    print p.registered(1)
    p.unregister(1)
    print not p.registered(1)

# Test epoll object when it is available.

try:
    from select import epoll
except ImportError:
    pass
else:
    print "creating epoll object"
    p = epoll()
    try:
        # Try to register and unregister a fd.
       
