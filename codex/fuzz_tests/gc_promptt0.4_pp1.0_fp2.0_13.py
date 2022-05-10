import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref callback that raises an exception.
# This used to cause a segfault.

# This is a simplified version of the test case that caused the segfault.
# The original test case was a bit more complicated, but it was not
# possible to reduce it to a small test case.  This version is
# simplified by using a single global object that is referenced by
# the weakref callback.  In the original test case, the object was
# created inside the callback, and the callback was called multiple
# times.

class A:
    pass

def callback(r):
    a = r()
    print a

a = A()
r = weakref.ref(a, callback)
del a
gc.collect()

# The original test case caused a segfault because the weakref callback
# was called during the sweep phase of the garbage collection.  The
# callback tried to create a new object, but the object allocation
# code tried to call PyObject_InitVar() on the object, which was
# already being freed.  The fix was to check for this case and ignore
