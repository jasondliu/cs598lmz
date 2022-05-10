import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect and gc.garbage
print(gc.collect())
print(gc.garbage)
# Test that gc collects only collectable objects (cyclic garbage is treated as non-garbage)
if 1:   # Enable this block for a good test
    class C1:
        def __init__(self, a):
            self.a = a
        def __repr__(self):
            return repr(self.a)
    class C2:
        def __init__(self, b):
            self.b = b
        def __repr__(self):
            return repr(self.b)
    c1 = C1(C2(C1(None)))
    del c1
    print(gc.collect())
    print(gc.garbage)

# Test that gc collects cyclic garbage
class C1:
    def __init__(self, a):
        self.a = a
    def __repr__(self):
        return repr(self.a)
class C2:
    def __init__(self, b):
        self.b
