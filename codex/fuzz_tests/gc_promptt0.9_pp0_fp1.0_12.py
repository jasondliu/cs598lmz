import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs whose callables change self.called.

called = []

class Callable:
    def __init__(self):
        self.called = 0

    def __call__(self):
        self.called = 1

ob1 = Callable()
w = weakref.ref(ob1, ob1)
gc.collect()
del ob1
gc.collect()
if w() is None or not w().called:
    raise TestFailed

del w
gc.collect()

# Test weakrefs to bound methods.

class C:
    pass

c = C()
c.__dict__["meth"] = c.meth = lambda: None
c.__dict__["wr"] = c.wr = weakref.ref(c.meth, lambda _ : None)

gc.collect()
del c
gc.collect()


# Test weakrefs to objects with cycles
class A:
    def __init__(self):
        self.ref = weakref.ref(self, self.del_self)
        self.a =
