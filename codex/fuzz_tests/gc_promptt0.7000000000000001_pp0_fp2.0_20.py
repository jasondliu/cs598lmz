import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() when a class has a weakrefable method.

class A(object):
    def __del__(self):
        pass

class B(object):
    def __del__(self):
        pass

    def meth(self):
        return A()

def f():
    b = B()
    gc.collect()
    # b must be tracked by the collector, because it has a method that
    # returns a weakly referencable object.  (This used to crash Python.)
    return weakref.ref(b)

f()()
