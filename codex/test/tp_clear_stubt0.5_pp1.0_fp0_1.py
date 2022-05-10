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
assert not latefin.ref(), "latefin.ref() is not dead"

# ____________________________________________________________

import gc, weakref

class A:
    pass

class B:
    pass

def func():
    pass

a = A()
b = B()
a.b = b
b.a = a
b.func = func
func.b = b
del a, b, func

gc.collect()
assert not func.b, "func.b is not dead"

# ____________________________________________________________

import gc, weakref

class A:
    pass

class B:
    pass

def func():
    pass

a = A()
b = B()
a.b = b
b.a = a
b.func = func
func.b = b
del a, b, func

gc.collect()
assert not func.b, "func.b is not dead"

# ____________________________________________________________

import gc, weakref

class A:
    pass

