import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect(0) vs gc.collect(1)
# Patch for defect 172177, fixed in 2.0
class G:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def meth(self, x):
        return self.x + x
class H:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def meth(self, s):
        return self.a + s
class I:
    def __init__(self, x, y):
        self.o = G(x, y)
    def __repr__(self):
        return repr(self.o)
class S:
    def __init__(self, a, b):
        self.o = H(a, b)
    def __repr__(self):
        return repr(self.o)
class D(S, I):
    pass

# Create a bunch of instances to exercise a number of conditions.
# If all instances die at the right time, this only
