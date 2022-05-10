import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
# Test weakref.ref()

class A:
    def __init__(self):
        self.b = B(self)

class B:
    def __init__(self, a):
        self.a = a
        self.wr = weakref.ref(a)

a = A()
#print a.b.wr()
del a
print gc.collect()
#print a.b.wr()
