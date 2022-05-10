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
del latefin
gc.collect()

# ____________________________________________________________

class A:
    pass

class B:
    pass

def f(a, b, c):
    return a, b, c

def g(a, b, c):
    return a, b, c

def h(a, b, c):
    return a, b, c

def i(a, b, c):
    return a, b, c

def j(a, b, c):
    return a, b, c

def k(a, b, c):
    return a, b, c

def l(a, b, c):
    return a, b, c

def m(a, b, c):
    return a, b, c

def n(a, b, c):
    return a, b, c

def o(a, b, c):
    return a, b, c

def p(a, b, c):
    return a, b, c

def q(a, b
