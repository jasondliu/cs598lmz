import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a cyclic reference.

class A:
    pass

a = A()
a.b = a

ref = weakref.ref(a)

# The following line is needed to trigger a bug in Python 2.3
a.b = None

del a

gc.collect()

if ref() is not None:
    print "a is not yet collected"
else:
    print "a is collected"

gc.collect()

if ref() is not None:
    print "a is not yet collected"
else:
    print "a is collected"
