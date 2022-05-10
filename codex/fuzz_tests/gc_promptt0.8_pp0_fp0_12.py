import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect in the presence of weakrefs.

import operator, sys

class C(object):
    pass

print "testing collect of weakrefs..."

# Create a cycle with a "normal" reference and a weak reference
c = C()
w = weakref.ref(c)
c.c = c

if gc.collect() != 1:
    print "collect didn't collect the cycle"
    sys.exit(1)

if w() is not None:
    print "collect didn't break the cycle"
    sys.exit(1)

# Create a cycle with two weak references
c = C()
w1 = weakref.ref(c)
w2 = weakref.ref(c)
c.c = c

if gc.collect() != 1:
    print "collect didn't collect the cycle"
    sys.exit(1)

if w1() is not None:
    print "collect didn't break the cycle"
    sys.exit(1)

if w2() is not None:
    print "collect didn't break the cycle"
   
