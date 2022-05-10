import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref callback that raises an exception.
# This used to cause a segfault.

class A:
    pass

def callback(w):
    raise ValueError

def f():
    a = A()
    wr = weakref.ref(a, callback)
    del a
    gc.collect()

f()
