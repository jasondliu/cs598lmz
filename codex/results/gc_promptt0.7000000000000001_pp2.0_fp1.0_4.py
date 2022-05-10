import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs
#
# This test *must* be run with the Python debug build
# (python_d.exe).  It is also helpful if gc.set_debug()
# is called with DEBUG_LEAK flags prior to running.

# Create some cyclic trash and make sure it gets collected
def f():
    l = [{}, {}, {}]
    l[1] = l
    wr = weakref.ref(l)
    del l
    return wr

wr = f()
del f
gc.collect()
print(wr(), wr() is None)


def f():
    l = [{}, {}, {}]
    l[1] = l
    return weakref.ref(l)

wr = f()
del f
gc.collect()
print(wr(), wr() is None)


def f():
    l = [{}, {}, {}]
    l[1] = l
    return weakref.ref(l)

wr = f()
del f
gc.collect()
print(wr(), wr() is None)



