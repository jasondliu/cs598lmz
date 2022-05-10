import weakref
# Test weakref.ref()
import sys
import os

class C(object):
    pass

c = C()
r = weakref.ref(c)
print type(r)
print r() is c

print "Creating cycle..."
l = [c]
c.x = l

print "clearing references..."
del c, l

print "Collecting..."
for i in range(5):
    collected = gc.collect()
    print "Garbage:", collected,
    print "Unreachable:", len(gc.garbage)
    print "Remaining refs:", len(gc.get_referrers(r))

print
print "Creating 1000000 weakrefs to int..."
r = weakref.ref(0)
for i in range(1000000):
    r()
if sys.platform == "win32":
    # XXX This test leaks on Windows.
    # XXX (But it's not easy to fix, because weakrefs to ints
    # XXX  can't be collected.)
    print "Leaking, so test is inconclusive"
    sys.exit
