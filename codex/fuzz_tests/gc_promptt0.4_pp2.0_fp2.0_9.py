import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref callback that triggers a gc.collect()
# recursively.  The second gc.collect() should not cause a segfault.
# See http://bugs.python.org/issue2456.

class A(object):
    pass

class B(object):
    pass

def callback(x):
    gc.collect()

a = A()
b = B()

a.b = b
b.a = a

a_wr = weakref.ref(a, callback)
del a, b

gc.collect()
gc.collect()
gc.collect()
