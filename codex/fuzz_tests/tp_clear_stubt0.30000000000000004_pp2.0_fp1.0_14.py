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

f = latefin.ref()

# Check that the cyclic garbage collector can handle the
# __del__ method of a weakref.

import gc, weakref

class A:
    def __init__(self, x):
        self.x = x
    def __del__(self):
        self.x = None

a = A(42)
r = weakref.ref(a)

del a
gc.collect()

print(r().x)

# Check that the cyclic garbage collector can handle the
# __del__ method of a weakref with a callback.

import gc, weakref

class A:
    def __init__(self, x):
        self.x = x
    def __del__(self):
        self.x = None

a = A(42)
r = weakref.ref(a, lambda x: None)

del a
gc.collect()

print(r().x)

# Check that the cyclic garbage collector can handle the
# __del__ method of
