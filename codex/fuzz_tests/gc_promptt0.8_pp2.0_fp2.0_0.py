import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs

class A:
    pass

a = A()
w = weakref.ref(a)
assert w() is a

gc.collect()
assert w() is a

del a
gc.collect()
assert w() is None

a = A()
w = weakref.ref(a)
assert w() is a

gc.collect()
assert w() is a

del a
del w
gc.collect()

# Test gc.collect() with weakref callbacks

class CallBack:
    def __init__(self, number):
        self.number = number
    def __call__(self, wr):
        l.append(self.number)

l = []
a = A()
w1 = weakref.ref(a, CallBack(1))
w2 = weakref.ref(a, CallBack(2))
assert a.__weakref__ is not None
assert w1() is a
assert w2() is a

gc.collect()
assert len(l) == 0

del a
gc.
