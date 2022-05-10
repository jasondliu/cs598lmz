import gc, weakref

class LateFin:
    __slots__ = ('ref',)
    def __del__(self):
        global func
        func = self.ref()

class Cyclic(tuple):
    __slots__ = ()
    def __del__(self):
        self[1].ref = weakref.ref(self[0])
        global latefin
        del latefin

latefin = LateFin()
func = lambda: None
cyc = tuple.__new__(Cyclic, (func, latefin))

func.__module__ = cyc
del func, cyc
gc.collect()

# Test that the weakref callback is not called immediately
assert latefin.ref() is not None

gc.collect()

# Test that the weakref callback is called when the object is destroyed
del latefin
gc.collect()

assert func() is None

# Test that the weakref callback is called when the object is destroyed
del func
gc.collect()

# If this test passed, then the weakref callback was called
# and the object was destroyed.
print("passed")
