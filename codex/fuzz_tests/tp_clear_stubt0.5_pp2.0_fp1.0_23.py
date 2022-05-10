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

# Issue #14763: a __del__ method that triggers GC should not resurrect objects
# that were weakly reachable to begin with.

class A:
    def __del__(self):
        gc.collect()

a = A()
b = A()
a.b = b
b.a = a
del a, b
gc.collect()

# Issue #14763: a __del__ method that triggers GC should not resurrect objects
# that were weakly reachable to begin with.

class A:
    def __del__(self):
        gc.collect()

a = A()
b = A()
a.b = b
b.a = a
del a, b
gc.collect()
