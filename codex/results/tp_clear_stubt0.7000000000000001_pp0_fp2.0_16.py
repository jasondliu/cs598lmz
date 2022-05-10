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

# This is a different test than the one above.  Here we create a
# cycle, and then try to delete the thing in the middle.  The
# previous test was designed to delete the thing in the middle, and
# then create a cycle.

class A:
    def __del__(self):
        self.b = B()

class B:
    def __del__(self):
        self.a = A()

del a, b
a = A()
b = B()

del a, b
gc.collect()
