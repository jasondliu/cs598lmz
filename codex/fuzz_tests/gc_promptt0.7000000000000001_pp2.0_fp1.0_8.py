import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect with a finalizer.
# This used to crash the interpreter.

# verify that the object is collectable
def f():
    print "called"
    # should not change the collectability
    gc.collect()

a = []
weakref.ref(a, f)

# should call the finalizer
del a
gc.collect()
