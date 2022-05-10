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
_ = gc.collect()

del latefin
_ = gc.collect()

# ____________________________________________________________

def f():
    pass

class X(object):
    def __del__(self):
        f()
        f()

def g():
    x = X()

g()
g()

# ____________________________________________________________

class X:
    def __del__(self):
        pass
    def __repr__(self):
        return "<X>"

class Y:
    def __del__(self):
        pass
    def __repr__(self):
        return "<Y>"

a = []
for i in range(10):
    a.append(X())

for i in range(20):
    a.append(Y())

del a[3::3]

import gc
gc.collect()

# ____________________________________________________________

class X:
    def __del__(self):
        pass
    def __repr__(self):
        return "<X>"

class Y:

