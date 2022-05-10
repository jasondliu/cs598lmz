import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect
#
# Weakrefs are created before the object is collected.
# The weakref callback should be invoked before gc.collect returns.

import weakref
class C:
    pass

def f(x):
    print "f", repr(x), x.alive

def g(x):
    print "g", repr(x), x.alive

for i in range(50):
    obj = C()
    obj.alive = True
    wr = weakref.ref(obj, f)
    wr2 = weakref.ref(obj, g)
    obj.alive = False
    del obj
    print "before collect"
    gc.collect()
    print "after collect"
    print
