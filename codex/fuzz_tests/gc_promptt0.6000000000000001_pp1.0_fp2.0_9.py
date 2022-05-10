import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() when a weakref to a weakrefable object is
# present.  This failed in Python 2.2: the weakrefable object was
# never collected because the weakref was still present.
class A(object):
    pass
def g():
    a = A()
    wr = weakref.ref(a)
    del a
    gc.collect()
    if wr() is not None:
        raise RuntimeError("object not collected")
    gc.set_debug(gc.DEBUG_UNCOLLECTABLE)
    print "OK"
g()
