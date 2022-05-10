import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect
a = {}
a[1] = a
del a
gc.collect()

# Test cyclic gc.
a = {}
w = weakref.ref(a)
a[1] = a
del a
gc.collect()

# Test gc of objects with __del__
# XXX Doesn't work on Linux debug builds (issue #1398)
class A:
    def __del__(self):
        pass
a = A()
w = weakref.ref(a)
del a
gc.collect()
w()
