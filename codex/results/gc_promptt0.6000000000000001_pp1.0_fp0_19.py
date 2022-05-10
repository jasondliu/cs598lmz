import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() vs. gc.collect(2)

class C:
    pass

# This function returns an object with a finalizer.
def f():
    x = C()
    x.a = x
    return x

# This function returns an object without a finalizer.
def g():
    x = C()
    x.a = x
    return weakref.ref(x)()

# This function returns an object with a finalizer, but
# it's only reachable as a callback from the weakref.
def h():
    x = C()
    x.a = weakref.ref(x)
    return x

def finalize(obj):
    print "finalizing", obj

# This function returns an object with a finalizer, and
# it's reachable as a callback from the weakref, but the
# weakref callback is called first.
def j():
    x = C()
    x.a = weakref.ref(x, finalize)
    return x

def test_collect():
    x = f()
    y = g()
   
