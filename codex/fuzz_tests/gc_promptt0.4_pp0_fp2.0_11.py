import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() when the only reference to the object is in a
# weakref.

class C:
    pass

def f():
    c = C()
    wr = weakref.ref(c)
    print "wr:", wr()
    del c
    print "wr:", wr()
    gc.collect()
    print "wr:", wr()

f()
print "gc.garbage:", gc.garbage
