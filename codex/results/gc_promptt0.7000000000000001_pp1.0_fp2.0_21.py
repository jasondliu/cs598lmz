import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with uncollectable objects.
# Result is 5, after 3 full collections (which is correct), because
# the weak references to X1, X2 and X3 have not yet been collected by
# the time gc.collect() is called.  They are collected by the next
# full collection.

class X:
    pass

class Y:
    pass

X1 = X()
X2 = X()
X3 = X()

# create a cycle
X1.attr = X2
X2.attr = X3
X3.attr = X1

# create a weakref
weakref.ref(X1)
weakref.ref(X2)
weakref.ref(X3)

# create a finalizer
Y1 = Y()
Y1.attr = X1
def finalize(obj):
    global Y1
    Y1 = None
gc.add_finalizer(Y1, finalize)

# check if the finalizer has been called yet
assert Y1.attr is X1

# create another finalizer
Y2 = Y()
Y
