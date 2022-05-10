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

# Check that the cyclic gc triggered by the __del__ method above
# has had a chance to run.
assert latefin.ref() is None

# This test checks that the cyclic gc handles the case where a
# __del__ method creates a new reference cycle involving an object
# with a __del__ method.
class C:
    def __del__(self):
        self.cycle = self

ob = C()
del ob
gc.collect()

# This test checks that the cyclic gc handles the case where a
# __del__ method mutates a list, changing one of its items to be
# equal to the list itself.
class C:
    def __del__(self):
        self.mutate()

class D(list):
    def mutate(self):
        self[:] = [self]

ob = C()
ob.mutate = D([1, ob]).mutate
del D, ob
gc.collect()

# This test checks that the cyclic gc handles the case where a
# __del__
