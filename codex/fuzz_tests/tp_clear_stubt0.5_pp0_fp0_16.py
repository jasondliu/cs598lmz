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
assert not latefin.ref(), "__del__ not called"

# Issue #5061: crash when __del__ triggers a weakref callback that
# triggers a GC collection

import gc, weakref

class A:
    pass

class B:
    pass

class C(A):
    def __del__(self):
        B()

def callback(ref):
    B()

a = A()
wref = weakref.ref(a, callback)
del wref
del a

gc.collect()

# Issue #5108: crash when __del__ triggers a weakref callback that
# triggers a GC collection, but with a cycle

import gc, weakref

class A:
    pass

class B:
    pass

class C(A):
    def __del__(self):
        B()

def callback(ref):
    B()

a = A()
wref = weakref.ref(a, callback)
a.wref = wref
del wref
del a


