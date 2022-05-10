import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a simple cyclic structure.
# This test is non-deterministic because of gc's randomization.

class A:
    def __init__(self):
        self.b = B(self)
        self.wref = weakref.ref(self)

class B:
    def __init__(self, a):
        self.a = a

def test():
    a = A()
    del a
    gc.collect()

if __name__ == "__main__":
    test()
