import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() on weakrefs to objects with __del__ methods.
# This used to crash in 2.2.

class A:
    def __del__(self):
        pass

a = A()
w = weakref.ref(a)

gc.collect()

# Test that a weakref callback can create new weakrefs to the object
# for which the callback was called.  This used to crash in 2.2.

class B:
    pass

def callback(w):
    x = B()
    # Create a new weakref to the object for which the callback was called.
    wr = weakref.ref(w(), callback)

b = B()
wr = weakref.ref(b, callback)
del b
gc.collect()

# Test that a weakref callback can create new weakrefs to the object
# for which the callback was called, and that the new weakrefs are
# processed before the callback is called again.  This used to crash
# in 2.2.

class C:
    pass

def callback(w):
    wr = weak
