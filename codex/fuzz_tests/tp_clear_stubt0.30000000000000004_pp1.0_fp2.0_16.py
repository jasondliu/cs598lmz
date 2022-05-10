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

# ____________________________________________________________

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

def f(x):
    return x.__class__

def g(x):
    return x.__class__.__bases__

def h(x):
    return x.__class__.__bases__[0]

def i(x):
    return x.__class__.__bases__[0].__bases__

def j(x):
    return x.__class__.__bases__[0].__bases__[0]

def k(x):
    return x.__class__.__bases__[0].__bases__[0].__bases__

def l(x):
    return x.__class__.__bases__[0].__bases__[0].__bases__[0]

def m(x):
    return x.__class__.
