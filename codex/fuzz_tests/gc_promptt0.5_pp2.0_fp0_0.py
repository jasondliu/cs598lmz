import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs to objects with __del__ methods
#
# The first test case is a reference cycle involving two objects with
# __del__ methods.  The weakref should break the cycle and allow the
# objects to be collected.

class A:
    def __init__(self):
        self.b = B(self)
        self.wr = weakref.ref(self.b, self.callback)
    def callback(self, wr):
        self.wr = None
    def __del__(self):
        pass

class B:
    def __init__(self, a):
        self.a = a
    def __del__(self):
        pass

def test():
    a = A()
    gc.collect()
    assert a.wr() is None
    assert gc.collect() == 0

test()

# The second test case is a reference cycle involving two objects with
# __del__ methods, where the weakref is not in the cycle.  The weakref
# should break the cycle and allow the objects to be collected.

class C:
