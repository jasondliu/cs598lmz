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

# Check that the cyclic garbage collector can break a reference cycle
# involving a __del__ method.  This test should not create a reference
# cycle.
class C:
    def __init__(self, n):
        self.n = n
        global x
        x = self
    def __del__(self):
        global y
        y = self.n

def f():
    C(1)

f()
del x
gc.collect()
assert y == 1


# Check that the cyclic garbage collector can break a reference cycle
# involving a __del__ method and a weakref.
# This test should not create a reference cycle.
class D:
    def __init__(self, n):
        self.n = n
        global x
        x = self
    def __del__(self):
        global y
        y = self.n

def g():
    d = D(1)
    import weakref
    wr = weakref.ref(d)
    del d
    return wr

wr = g()

