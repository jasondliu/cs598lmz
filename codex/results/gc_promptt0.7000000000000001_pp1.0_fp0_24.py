import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() when a finalizer is scheduled to run
# but not yet run and the object is resurrected.

def f(x):
    print "calling f", x
    n = len(gc.garbage)
    del x
    print "f sees", len(gc.garbage), "in garbage"
    assert len(gc.garbage) == n

class C(object):
    pass

c = C()
wr = weakref.ref(c, f)

print gc.collect()

del c

print gc.collect()

assert len(gc.garbage) == 1

c = gc.garbage.pop()

# resurrect c
del c
